# Node-RED project flows

`flows.json` contains the Node-RED implementation used to document and reproduce the Autonomic Lift Truck dashboard and Self-CHOP logic.

## Included tabs

1. **Dashboard + Self-Healing**
   - Speed display.
   - Boolean stuck logic: `StatusAlert = A AND NOT B`, where `A` is derived from odometry and `B` from LiDAR/scan behavior.
   - Virtual LED: green = no stuck condition; red = stuck condition.
   - Project MQTT topics: `robot/battery` and `factory/orders`.
   - Battery gauge converts voltage to percentage. `BATTERY_FULL_V` and `BATTERY_EMPTY_V` are exposed as configuration values for the target sensor/battery calibration.
   - `ODOM_SPEED_THRESHOLD` and `SCAN_MOTION_THRESHOLD` are also configurable for the hardware environment.

2. **Self-Optimization**
   - Implements the project speed law `Sf = 0.02 + 0.02 B`, where `B` is the number of queued orders.
   - The manuscript reports that `B` was limited to 10 during testing. Override with `MAX_TEST_ORDERS` if required.
   - Publishes target speed to `robot/target_speed` as an adapter topic.

3. **AES-256-CBC Self-Protection**
   - Implements the project AES-256-CBC encryption/decryption pattern using Node.js `crypto`.
   - The project passkey is intentionally **not distributed** in this repository.
   - Set `AES_KEY` to an exactly 32-byte UTF-8 key. The flow has no embedded/default key and rejects a missing or incorrectly sized value.
   - Encrypted messages use the `IV:ciphertext` hexadecimal format used by the project logic.
   - Demonstration MQTT topic: `autonomic_lift_truck/secure_demo`.

## Dependencies

- Node-RED
- `node-red-dashboard` for the dashboard nodes.
- An MQTT broker (the included broker configuration defaults to `localhost:1883`; edit it for the target installation).
- Function-node external modules must permit the built-in Node.js `crypto` module for the AES tab.

## ROS integration

The project implementation uses `/odom` and LiDAR/scan information for the stuck detector. The repository flow exposes portable MQTT adapter inputs `robot/odom_speed` and `robot/scan_motion`; these can be fed by the ROS installation or replaced with the target installation's ROS subscription nodes.

## Security

Before running the AES tab, set a new 32-byte key, for example:

```bash
export AES_KEY="$(openssl rand -hex 16)"
```

Do not publish or reuse a production key.
