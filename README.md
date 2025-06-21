# Saleae_Logic_HLA
Saleae Logic 2 High Level Analyzers

## EmbeddedVideoEngine5
A decoder for the SPI traffic to/from BT820 chips from Bridgetek.

Not perfect, but a whole lot better than raw data, decodes host commands, knows the differences between READ and WRITE access, decodes registers, decodes the status when reading from REG_BOOT_STATUS, detects access to RAM-DL, tries to decode the first command word when writing to RAM-DL or REG_CMDB_WRITE...

