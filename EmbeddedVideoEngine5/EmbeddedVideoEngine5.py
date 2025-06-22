# High Level Analyzer for BT82x chips from Bridgetek
#@version 1.0
#@date    2025-06-22
#@author  Rudolph Riedel

#MIT License
#
#Copyright (c) 2016-2025 Rudolph Riedel
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the "Software"), to deal in
#the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense,
#and/or sell copies of the Software, and to permit persons to whom the Software
#is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
#FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
#COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
#IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
#CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# For more information and documentation, please go to https://support.saleae.com/extensions/high-level-analyzer-extensions


from saleae.analyzers import HighLevelAnalyzer, AnalyzerFrame

# host command codes
COMMANDS = {
    0xE0: "STANDBY",
    0xE1: "SLEEP",
    0xE2: "PWRDOWN",
    0xE4: "SETPLLSP1",
    0xE6: "SETSYSCLKDIV",
    0xE7: "RESET_PULSE",
    0xE8: "SETTBOOTCFG",
    0xE9: "BOOTCFGEN",
    0xEB: "SETDDRTYPE"
}

# register names
REGISTERS = {
    0x7F004000: "REG_TRACKER",
    0x7F004004: "REG_TRACKER_1",
    0x7F004008: "REG_TRACKER_2",
    0x7F00400C: "REG_TRACKER_3",
    0x7F004010: "REG_TRACKER_4",
    0x7F004014: "REG_MEDIAFIFO_READ",
    0x7F004018: "REG_MEDIAFIFO_WRITE",
    0x7F004024: "REG_FLASH_SIZE",
    0x7F00402C: "REG_ANIM_ACTIVE",
    0x7F004038: "REG_OBJECT_COMPLETE",
    0x7F00403C: "REG_EXTENT_X0",
    0x7F004040: "REG_EXTENT_Y0",
    0x7F004044: "REG_EXTENT_X1",
    0x7F004048: "REG_EXTENT_Y1",
    0x7F004050: "REG_PLAY_CONTROL",
    0x7F006000: "REG_ID",
    0x7F006004: "REG_FRAMES",
    0x7F006008: "REG_CLOCK",
    0x7F00600C: "REG_FREQUENCY",
    0x7F006010: "REG_RE_DEST",
    0x7F006014: "REG_RE_FORMAT",
    0x7F006018: "REG_RE_ROTATE",
    0x7F00601C: "REG_RE_W",
    0x7F006020: "REG_RE_H",
    0x7F006024: "REG_RE_DITHER",
    0x7F006028: "REG_RE_ACTIVE",
    0x7F00602C: "REG_RE_RENDERS",
    0x7F006034: "REG_SC0_RESET",
    0x7F006038: "REG_SC0_SIZE",
    0x7F00603C: "REG_SC0_PTR0",
    0x7F006040: "REG_SC0_PTR1",
    0x7F006044: "REG_SC0_PTR2",
    0x7F006048: "REG_SC0_PTR3",
    0x7F00604C: "REG_SC1_RESET",
    0x7F006050: "REG_SC1_SIZE",
    0x7F006054: "REG_SC1_PTR0",
    0x7F006058: "REG_SC1_PTR1",
    0x7F00605C: "REG_SC1_PTR2",
    0x7F006060: "REG_SC1_PTR3",
    0x7F006064: "REG_SC2_RESET",
    0x7F006068: "REG_SC2_SIZE",
    0x7F00606C: "REG_SC2_PTR0",
    0x7F006070: "REG_SC2_PTR1",
    0x7F006074: "REG_SC2_PTR2",
    0x7F006078: "REG_SC2_PTR3",
    0x7F006088: "REG_CPURESET",
    0x7F00608C: "REG_HCYCLE",
    0x7F006090: "REG_HOFFSET",
    0x7F006094: "REG_HSIZE",
    0x7F006098: "REG_HSYNC0",
    0x7F00609C: "REG_HSYNC1",
    0x7F0060A0: "REG_VCYCLE",
    0x7F0060A4: "REG_VOFFSET",
    0x7F0060A8: "REG_VSIZE",
    0x7F0060AC: "REG_VSYNC0",
    0x7F0060B0: "REG_VSYNC1",
    0x7F0060B4: "REG_DLSWAP",
    0x7F0060B8: "REG_PCLK_POL",
    0x7F0060BC: "REG_TAG_X",
    0x7F0060C0: "REG_TAG_Y",
    0x7F0060C4: "REG_TAG",
    0x7F0060C8: "REG_VOL_L_PB",
    0x7F0060CC: "REG_VOL_R_PB",
    0x7F0060D0: "REG_VOL_SOUND",
    0x7F0060D4: "REG_SOUND",
    0x7F0060D8: "REG_PLAY",
    0x7F0060DC: "REG_GPIO_DIR",
    0x7F0060E0: "REG_GPIO",
    0x7F0060E4: "REG_DISP",
    0x7F006100: "REG_INT_FLAGS",
    0x7F006104: "REG_INT_EN",
    0x7F006108: "REG_INT_MASK",
    0x7F00610C: "REG_PLAYBACK_START",
    0x7F006110: "REG_PLAYBACK_LENGTH",
    0x7F006114: "REG_PLAYBACK_READPTR",
    0x7F006118: "REG_PLAYBACK_FREQ",
    0x7F00611C: "REG_PLAYBACK_FORMAT",
    0x7F006120: "REG_PLAYBACK_LOOP",
    0x7F006124: "REG_PLAYBACK_PLAY",
    0x7F006128: "REG_PWM_HZ",
    0x7F00612C: "REG_PWM_DUTY",
    0x7F006130: "REG_MACRO_0",
    0x7F006134: "REG_MACRO_1",
    0x7F00613C: "REG_AUD_PWM",
    0x7F00614C: "REG_CMD_READ",
    0x7F006150: "REG_CMD_WRITE",
    0x7F006154: "REG_CMD_DL",
    0x7F006158: "REG_TOUCH_MODE",
    0x7F00615C: "REG_CTOUCH_EXTENDED",
    0x7F006160: "REG_TOUCH_SCREEN_XY",
    0x7F006164: "REG_TOUCH_RAW_XY",
    0x7F006168: "REG_CTOUCH_TOUCHB_XY",
    0x7F00616C: "REG_CTOUCH_TOUCHC_XY",
    0x7F006170: "REG_CTOUCH_TOUCH4_XY",
    0x7F006174: "REG_TOUCH_TAG_XY",
    0x7F006178: "REG_TOUCH_TAG",
    0x7F00617C: "REG_TOUCH_TAG1_XY",
    0x7F006180: "REG_TOUCH_TAG1",
    0x7F006184: "REG_TOUCH_TAG2_XY",
    0x7F006188: "REG_TOUCH_TAG2",
    0x7F00618C: "REG_TOUCH_TAG3_XY",
    0x7F006190: "REG_TOUCH_TAG3",
    0x7F006194: "REG_TOUCH_TAG4_XY",
    0x7F006198: "REG_TOUCH_TAG4",
    0x7F00619C: "REG_TOUCH_TRANSFORM_A",
    0x7F0061A0: "REG_TOUCH_TRANSFORM_B",
    0x7F0061A4: "REG_TOUCH_TRANSFORM_C",
    0x7F0061A8: "REG_TOUCH_TRANSFORM_D",
    0x7F0061AC: "REG_TOUCH_TRANSFORM_E",
    0x7F0061B0: "REG_TOUCH_TRANSFORM_F",
    0x7F0061B4: "REG_TOUCH_CONFIG",
    0x7F006594: "REG_CMDB_SPACE",
    0x7F0065D0: "REG_PLAYBACK_PAUSE",
    0x7F0065D4: "REG_FLASH_STATUS",
    0x7F0065F4: "REG_SO_MODE",
    0x7F0065F8: "REG_SO_SOURCE",
    0x7F0065FC: "REG_SO_FORMAT",
    0x7F006600: "REG_SO_EN",
    0x7F006628: "REG_BOOT_CFG",
    0x7F006670: "REG_LVDSRX_CORE_ENABLE",
    0x7F006674: "REG_LVDSRX_CORE_CAPTURE",
    0x7F006678: "REG_LVDSRX_CORE_SETUP",
    0x7F00667C: "REG_LVDSRX_CORE_DEST",
    0x7F006680: "REG_LVDSRX_CORE_FORMAT",
    0x7F006684: "REG_LVDSRX_CORE_DITHER",
    0x7F006698: "REG_LVDSRX_CORE_FRAMES",
    0x7F006714: "REG_I2S_EN",
    0x7F006718: "REG_I2S_FREQ",
    0x7F006780: "REG_SC2_STATUS",
    0x7F006784: "REG_SC2_ADDR",
    0x7F010000: "REG_CMDB_WRITE",
    0x7F800300: "REG_LVDSTX_EN",
    0x7F800304: "REG_LVDSTX_PLLCFG",
    0x7F800314: "REG_LVDSTX_CTRL_CH0",
    0x7F800318: "REG_LVDSTX_CTRL_CH1",
    0x7F80031C: "REG_LVDSTX_STAT",
    0x7F800320: "REG_LVDSTX_ERR_STAT",
    0x7F800408: "REG_PIN_DRV_0",
    0x7F80040C: "REG_PIN_DRV_1",
    0x7F800410: "REG_PIN_SLEW_0",
    0x7F800414: "REG_PIN_TYPE_0",
    0x7F800418: "REG_PIN_TYPE_1",
    0x7F800420: "REG_SYS_CFG",
    0x7F800424: "REG_SYS_STAT",
    0x7F800448: "REG_CHIP_ID",
    0x7F80044C: "REG_BOOT_STATUS",
    0x7F800454: "REG_DDR_TYPE",
    0x7F800464: "REG_PIN_DRV_2",
    0x7F800468: "REG_PIN_SLEW_1",
    0x7F80046C: "REG_PIN_TYPE_2",
    0x7F800500: "REG_LVDSRX_SETUP",
    0x7F800504: "REG_LVDSRX_CTRL",
    0x7F800508: "REG_LVDSRX_STAT",
    0x7F800800: "REG_I2S_CFG",
    0x7F800804: "REG_I2S_CTL",
    0x7F800810: "REG_I2S_STAT",
    0x7F800814: "REG_I2S_PAD_CFG",
}

DL_COMMANDS = {
    0x00000000: "DL_DISPLAY",
    0x01000000: "DL_BITMAP_SOURCE",
    0x02000000: "DL_CLEAR_COLOR_RGB",
    0x03000000: "DL_TAG",
    0x04000000: "DL_COLOR_RGB",
    0x05000000: "DL_BITMAP_HANDLE",
    0x06000000: "DL_CELL",
    0x07000000: "DL_BITMAP_LAYOUT",
    0x08000000: "DL_BITMAP_SIZE",
    0x09000000: "DL_ALPHA_FUNC",
    0x0A000000: "DL_STENCIL_FUNC",
    0x0B000000: "DL_BLEND_FUNC",
    0x0C000000: "DL_STENCIL_OP",
    0x0D000000: "DL_POINT_SIZE",
    0x0E000000: "DL_LINE_WIDTH",
    0x0F000000: "DL_CLEAR_COLOR_A",
    0x10000000: "DL_COLOR_A",
    0x11000000: "DL_CLEAR_STENCIL",
    0x12000000: "DL_CLEAR_TAG",
    0x13000000: "DL_STENCIL_MASK",
    0x14000000: "DL_TAG_MASK",
    0x15000000: "DL_BITMAP_TRANSFORM_A",
    0x16000000: "DL_BITMAP_TRANSFORM_B",
    0x17000000: "DL_BITMAP_TRANSFORM_C",
    0x18000000: "DL_BITMAP_TRANSFORM_D",
    0x19000000: "DL_BITMAP_TRANSFORM_E",
    0x1A000000: "DL_BITMAP_TRANSFORM_F",
    0x1B000000: "DL_SCISSOR_XY",
    0x1C000000: "DL_SCISSOR_SIZE",
    0x1D000000: "DL_CALL",
    0x1E000000: "DL_JUMP",
    0x1F000000: "DL_BEGIN",
    0x20000000: "DL_COLOR_MASK",
    0x21000000: "DL_END",
    0x22000000: "DL_SAVE_CONTEXT",
    0x23000000: "DL_RESTORE_CONTEXT",
    0x24000000: "DL_RETURN",
    0x25000000: "DL_MACRO",
    0x26000000: "DL_CLEAR",
    0x27000000: "DL_VERTEX_FORMAT",
    0x28000000: "DL_BITMAP_LAYOUT_H",
    0x29000000: "DL_BITMAP_SIZE_H",
    0x2A000000: "DL_PALETTE_SOURCE",
    0x2B000000: "DL_VERTEX_TRANSLATE_X",
    0x2C000000: "DL_VERTEX_TRANSLATE_Y",
    0x2D000000: "DL_NOP",
    0x2E000000: "DL_BITMAP_EXT_FORMAT",
    0x2F000000: "DL_BITMAP_SWIZZLE",
    0x31000000: "DL_BITMAP_SOURCEH",
    0x32000000: "DL_PALETTE_SOURCEH",
    0x33000000: "DL_BITMAP_ZORDER",
    0x34000000: "DL_REGION",
}

COPRO_COMMANDS = {
    0xFFFFFF4F: "CMD_ANIMDRAW",
    0xFFFFFF5E: "CMD_ANIMFRAME",
    0xFFFFFF5F: "CMD_ANIMSTART",
    0xFFFFFF4D: "CMD_ANIMSTOP",
    0xFFFFFF4E: "CMD_ANIMXY",
    0xFFFFFF1C: "CMD_APPEND",
    0xFFFFFF52: "CMD_APPENDF",
    0xFFFFFF87: "CMD_ARC",
    0xFFFFFF07: "CMD_BGCOLOR",
    0xFFFFFF1F: "CMD_BITMAP_TRANSFORM",
    0xFFFFFF0B: "CMD_BUTTON",
    0xFFFFFF13: "CMD_CALIBRATE",
    0xFFFFFF56: "CMD_CALIBRATESUB",
    0xFFFFFF5B: "CMD_CALLLIST",
    0xFFFFFF8A: "CMD_CGRADIENT",
    0xFFFFFF12: "CMD_CLOCK",
    0xFFFFFF2E: "CMD_COLDSTART",
    0xFFFFFF88: "CMD_COPYLIST",
    0xFFFFFF65: "CMD_DDRSHUTDOWN",
    0xFFFFFF66: "CMD_DDRSTARTUP",
    0xFFFFFF29: "CMD_DIAL",
    0xFFFFFF00: "CMD_DLSTART",
    0xFFFFFF7E: "CMD_ENABLEREGION",
    0xFFFFFF5D: "CMD_ENDLIST",
    0xFFFFFF68: "CMD_FENCE",
    0xFFFFFF08: "CMD_FGCOLOR",
    0xFFFFFF51: "CMD_FILLWIDTH",
    0xFFFFFF43: "CMD_FLASHATTACH",
    0xFFFFFF42: "CMD_FLASHDETACH",
    0xFFFFFF3E: "CMD_FLASHERASE",
    0xFFFFFF44: "CMD_FLASHFAST",
    0xFFFFFF64: "CMD_FLASHPROGRAM",
    0xFFFFFF40: "CMD_FLASHREAD",
    0xFFFFFF48: "CMD_FLASHSOURCE",
    0xFFFFFF45: "CMD_FLASHSPIDESEL",
    0xFFFFFF47: "CMD_FLASHSPIRX",
    0xFFFFFF46: "CMD_FLASHSPITX",
    0xFFFFFF41: "CMD_FLASHUPDATE",
    0xFFFFFF3F: "CMD_FLASHWRITE",
    0xFFFFFF8E: "CMD_FSDIR",
    0xFFFFFF6D: "CMD_FSOPTIONS",
    0xFFFFFF71: "CMD_FSREAD",
    0xFFFFFF80: "CMD_FSSIZE",
    0xFFFFFF7F: "CMD_FSSOURCE",
    0xFFFFFF11: "CMD_GAUGE",
    0xFFFFFF58: "CMD_GETIMAGE",
    0xFFFFFF2F: "CMD_GETMATRIX",
    0xFFFFFF22: "CMD_GETPROPS",
    0xFFFFFF20: "CMD_GETPTR",
    0xFFFFFF8B: "CMD_GLOW",
    0xFFFFFF30: "CMD_GRADCOLOR",
    0xFFFFFF09: "CMD_GRADIENT",
    0xFFFFFF50: "CMD_GRADIENTA",
    0xFFFFFF6B: "CMD_GRAPHICSFINISH",
    0xFFFFFF69: "CMD_I2SSTARTUP",
    0xFFFFFF4A: "CMD_INFLATE",
    0xFFFFFF02: "CMD_INTERRUPT",
    0xFFFFFF0C: "CMD_KEYS",
    0xFFFFFF81: "CMD_LOADASSET",
    0xFFFFFF23: "CMD_LOADIDENTITY",
    0xFFFFFF21: "CMD_LOADIMAGE",
    0xFFFFFF85: "CMD_LOADWAV",
    0xFFFFFF2D: "CMD_LOGO",
    0xFFFFFF34: "CMD_MEDIAFIFO",
    0xFFFFFF1B: "CMD_MEMCPY",
    0xFFFFFF16: "CMD_MEMCRC",
    0xFFFFFF19: "CMD_MEMSET",
    0xFFFFFF18: "CMD_MEMWRITE",
    0xFFFFFF1A: "CMD_MEMZERO",
    0xFFFFFF5C: "CMD_NEWLIST",
    0xFFFFFF53: "CMD_NOP",
    0xFFFFFF2A: "CMD_NUMBER",
    0xFFFFFF35: "CMD_PLAYVIDEO",
    0xFFFFFF79: "CMD_PLAYWAV",
    0xFFFFFF0D: "CMD_PROGRESS",
    0xFFFFFF17: "CMD_REGREAD",
    0xFFFFFF86: "CMD_REGWRITE",
    0xFFFFFF8D: "CMD_RENDERTARGET",
    0xFFFFFF4C: "CMD_RESETFONTS",
    0xFFFFFF7D: "CMD_RESTORECONTEXT",
    0xFFFFFF89: "CMD_RESULT",
    0xFFFFFF5A: "CMD_RETURN",
    0xFFFFFF39: "CMD_ROMFONT",
    0xFFFFFF26: "CMD_ROTATE",
    0xFFFFFF4B: "CMD_ROTATEAROUND",
    0xFFFFFF60: "CMD_RUNANIM",
    0xFFFFFF7C: "CMD_SAVECONTEXT",
    0xFFFFFF25: "CMD_SCALE",
    0xFFFFFF2B: "CMD_SCREENSAVER",
    0xFFFFFF0F: "CMD_SCROLLBAR",
    0xFFFFFF6E: "CMD_SDATTACH",
    0xFFFFFF6F: "CMD_SDBLOCKREAD",
    0xFFFFFF33: "CMD_SETBASE",
    0xFFFFFF3D: "CMD_SETBITMAP",
    0xFFFFFF36: "CMD_SETFONT",
    0xFFFFFF27: "CMD_SETMATRIX",
    0xFFFFFF31: "CMD_SETROTATE",
    0xFFFFFF37: "CMD_SETSCRATCH",
    0xFFFFFF2C: "CMD_SKETCH",
    0xFFFFFF8C: "CMD_SKIPCOND",
    0xFFFFFF0E: "CMD_SLIDER",
    0xFFFFFF1D: "CMD_SNAPSHOT",
    0xFFFFFF14: "CMD_SPINNER",
    0xFFFFFF15: "CMD_STOP",
    0xFFFFFF01: "CMD_SWAP",
    0xFFFFFF3C: "CMD_SYNC",
    0xFFFFFF57: "CMD_TESTCARD",
    0xFFFFFF0A: "CMD_TEXT",
    0xFFFFFF84: "CMD_TEXTDIM",
    0xFFFFFF10: "CMD_TOGGLE",
    0xFFFFFF28: "CMD_TRACK",
    0xFFFFFF24: "CMD_TRANSLATE",
    0xFFFFFF3B: "CMD_VIDEOFRAME",
    0xFFFFFF3A: "CMD_VIDEOSTART",
    0xFFFFFF59: "CMD_WAIT",
    0xFFFFFF67: "CMD_WAITCHANGE",
    0xFFFFFF78: "CMD_WAITCOND",
    0xFFFFFF83: "CMD_WATCHDOG"
}

BOOT_STATUS = {
    "0x492E2E2E": "Coprocessor is running",
    "0x4F2E2E2E": "Read system configuration",
    "0x442E2E2E": "DDR initialization started",
    "0x444D3038": "DDR initialization, waiting for DDR initialization done",
    "0x44433035": "DDR initialization, waiting for DDR out of reset",
    "0x44553135": "DDR initialization, 150 us delay",
    "0x44553730": "DDR initialization, 700 us delay",
    "0x552E2E2E": "Decompressing rom main image to DDR",
    "0x432E2E2E": "Copying into program memory",
    "0x562E2E2E": "Decompressing rom asset image to DDR",
    "0x4C2E2E2E": "Initializing local variables",
    "0x542E2E2E": "Copying into touch program memory",
    "0x462E2E2E": "Attempting to attach to flash",
    "0x522E2E2E": "Normal running",
    "0x452E2E2E": "DDR shutdown started",
    "0x454D3130": "DDR shutdown, waiting for DDR enter self-refresh state",
    "0x45433034": "DDR shutdown, waiting for DDR enter reset",
    "0x5A2E2E2E": "DDR shutdown state",
    "0x572E2E2E": "DDR warm start, started",
    "0x57433035": "DDR warm start, waiting for DDR out of reset",
    "0x574D3038": "DDR warm start, waiting for DDR initialization done",
    "0x574D3130": "DDR warm start, waiting for DDR enter self-refresh state",
    "0x576D3130": "DDR warm start, waiting for DDR not in self-refresh state",
    "0x57553135": "DDR warm start, 150 us delay",
}

def decode_read_response(miso_buffer):
    """
    Finds sync byte (0x01) in MISO buffer, decodes the following
    1, 2, or 4 bytes (whichever applies) in reverse byte order.
    Returns formatted hex string or None.
    """
    miso_bytes = [b for _, _, b in miso_buffer]

    try:
        sync_index = miso_bytes.index(0x01)
    except ValueError:
        return None  # Sync byte not found

    data_bytes = miso_bytes[sync_index + 1:]
    data_len = len(data_bytes)

    # Try longest possible value first
    if data_len >= 4:
        length = 4
    elif data_len >= 2:
        length = 2
    elif data_len >= 1:
        length = 1
    else:
        return None  # No data after sync byte

    reversed_bytes = data_bytes[:length][::-1]
    value = 0
    for b in reversed_bytes:
        value = (value << 8) | b

    return f"0x{value:0{length * 2}X}"

def decode_write(mosi_buffer, number=0):
    """
    Decode a 32-bit write word from the MOSI buffer.

    Parameters:
    - mosi_buffer: list of (start_time, end_time, byte) tuples
    - number: which 32-bit word to decode, 0 = bytes 4..7, 1 = bytes 8..11, etc.

    Returns:
    - hex string like '0x12345678' or None if not enough bytes
    """
    # Calculate start index of the requested 32-bit word in buffer
    start_index = 4 + (number * 4)
    end_index = start_index + 4

    if len(mosi_buffer) < end_index:
        return None  # Not enough data for this word

    # Extract bytes
    word_bytes = [b for _, _, b in mosi_buffer[start_index:end_index]]

    # Reverse byte order (assuming little endian)
    word_bytes.reverse()

    # Convert bytes to integer
    value = 0
    for b in word_bytes:
        value = (value << 8) | b

    # Format as hex string
    return f"0x{value:08X}"

class Hla(HighLevelAnalyzer):
    result_types = {
        'active': {'format': 'ACTIVE'},
        'command': {'format': '{cmd_name}'},
    }

    def __init__(self):
        self.frame_buffer_mosi = []
        self.frame_buffer_miso = []
        self.frame_start_time = None

    def decode(self, frame: AnalyzerFrame):
        if frame.type == 'enable':
            self.frame_buffer_mosi = []
            self.frame_buffer_miso = []
            self.frame_start_time = frame.start_time
            return None

        elif frame.type == 'result':
            raw_mosi = frame.data.get('mosi')
            raw_miso = frame.data.get('miso')

            if (raw_mosi is None) or (raw_miso is None):
                return None

            mosi_byte = raw_mosi[0]
            miso_byte = raw_miso[0]

            self.frame_buffer_mosi.append((frame.start_time, frame.end_time, mosi_byte))
            self.frame_buffer_miso.append((frame.start_time, frame.end_time, miso_byte))

            return None

        elif frame.type == 'disable':
            if not self.frame_buffer_mosi:
                return None

            mosi_bytes = [b for (_, _, b) in self.frame_buffer_mosi]
            start_time = self.frame_start_time or self.frame_buffer_mosi[0][0]
            end_time = self.frame_buffer_mosi[-1][1]

            # Case 1: All 5 bytes are 0x00 -> ACTIVE
            if len(mosi_bytes) == 5 and all(b == 0x00 for b in mosi_bytes):
                return AnalyzerFrame('ACTIVE', start_time, end_time, {})

            # Case 2: Special 0xFF command frame
            if len(mosi_bytes) == 5 and mosi_bytes[0] == 0xFF and (mosi_bytes[1] & 0xF0) == 0xE0:
                cmd = mosi_bytes[1]
                cmd_name = COMMANDS.get(cmd, f"UNKNOWN_CMD (0x{cmd:02X})")
                return AnalyzerFrame(cmd_name, start_time, end_time, {})

            # Case 3: Read/Write frame
            if len(mosi_bytes) >= 4:
                addr = (
                    ((mosi_bytes[0] & 0x7f) << 24) |
                    (mosi_bytes[1] << 16) |
                    (mosi_bytes[2] << 8) |
                    mosi_bytes[3]
                )

                is_write = (mosi_bytes[0] & 0x80) != 0

                op = "WRITE" if (mosi_bytes[0] & 0x80) else "READ"

                # Resolve register label or dynamic RAM-DL offset
                if 0x7F008000 <= addr <= 0x7F00BFFF:
                    offset = addr - 0x7F008000
                    label = f"RAM-DL+0x{offset:04X}"
                else:
                    label = REGISTERS.get(addr, f"0x{addr:08X}")

                text = f"{op} {label}"

                if is_write:
                    # WRITE Frame
                    value_str = decode_write(self.frame_buffer_mosi, 0)

                    if label.startswith("RAM-DL+0x") or label == 'REG_CMDB_WRITE':
                        value_int = int(value_str, 16)
                        cmd_name = COPRO_COMMANDS.get(value_int, value_str)

                        if cmd_name != value_str:
                            value_str = cmd_name
                        else:
                            cmd_key = value_int & 0xFF000000
                            cmd_name = DL_COMMANDS.get(cmd_key)
                            if cmd_name:
                                value_str = f"{cmd_name} + 0x{value_int & 0x00FFFFFF:06X}"

                            if mosi_bytes[7] & 0xC0 == 0x40:
                                value_str = f"'DL_VERTEX2F' + 0x{value_int & 0x3FFFFFFF:08X}"

                            if mosi_bytes[7] & 0xC0 == 0x80:
                                value_str = f"'DL_VERTEX2II' + 0x{value_int & 0x3FFFFFFF:08X}"

                    return AnalyzerFrame(text, start_time, end_time, {
                        "data": value_str
                    })

                else:
                    # READ Frame
                    value_str = decode_read_response(self.frame_buffer_miso)

                    if label == 'REG_BOOT_STATUS':
                        value_str = BOOT_STATUS.get(value_str, value_str)

                    return AnalyzerFrame(text, start_time, end_time, {
                        "data": value_str or "READ_ERROR"
                    })

            return None
