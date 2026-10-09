# Project notes and software ownership

This repository distinguishes only between **project-owned materials** and **third-party dependencies**.

## Project-owned materials

The data tables, experimental media, analysis utilities, Node-RED flows, mapping helpers, documentation, and repository metadata included in this package are project materials prepared to support the reported results of manuscript `machines-4629373`.

The repository is organized for reproducibility and reuse. File names and folder locations are standardized for publication, and classification is based on ownership only.

## Security-related change

The Node-RED AES-256-CBC implementation follows the project encryption/decryption logic. For repository publication, the project passkey is **not distributed**. The flow reads a replacement 32-byte AES key from the `AES_KEY` environment variable. This is the intentional security-related change in the public package.

## Configurable runtime parameters

Hardware-dependent thresholds and broker settings are exposed as configuration values so that the flows can be run on another installation without embedding machine-specific settings. This includes odometry/scan thresholds, battery voltage limits, the MQTT broker address, and the AES key.

## Third-party dependencies

Third-party ROS/RRT/SLAM, TurtleBot3, Dynamixel, Node-RED, and related packages are not presented as project-owned source code. See `software/THIRD_PARTY.md` for the dependency list and source attribution.
