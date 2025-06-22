# High Level Analyzer for FT81x/BT81x chips from Bridgetek
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
    0x00: "ACTIVE",
    0x41: "STANDBY",
    0x42: "SLEEP",
    0x44: "CLKEXT",
    0x48: "CLKINT",
    0x50: "PWRDOWN",
    0x61: "CLKSEL",
    0x68: "RST_PULSE",
    0x70: "PINDRIVE",
    0x71: "PIN_PD_STATE"
}

REGISTERS = {
    0x00302000: "REG_ID",
    0x00302004: "REG_FRAMES",
    0x00302008: "REG_CLOCK",
    0x0030200C: "REG_FREQUENCY",
    0x00302010: "REG_RENDERMODE",
    0x00302014: "REG_SNAPY",
    0x00302018: "REG_SNAPSHOT",
    0x0030201C: "REG_SNAPFORMAT",
    0x00302020: "REG_CPURESET",
    0x00302024: "REG_TAP_CRC",
    0x00302028: "REG_TAP_MASK",
    0x0030202C: "REG_HCYCLE",
    0x00302030: "REG_HOFFSET",
    0x00302034: "REG_HSIZE",
    0x00302038: "REG_HSYNC0",
    0x0030203C: "REG_HSYNC1",
    0x00302040: "REG_VCYCLE",
    0x00302044: "REG_VOFFSET",
    0x00302048: "REG_VSIZE",
    0x0030204C: "REG_VSYNC0",
    0x00302050: "REG_VSYNC1",
    0x00302054: "REG_DLSWAP",
    0x00302058: "REG_ROTATE",
    0x0030205C: "REG_OUTBITS",
    0x00302060: "REG_DITHER",
    0x00302064: "REG_SWIZZLE",
    0x00302068: "REG_CSPREAD",
    0x0030206C: "REG_PCLK_POL",
    0x00302070: "REG_PCLK",
    0x00302074: "REG_TAG_X",
    0x00302078: "REG_TAG_Y",
    0x0030207C: "REG_TAG",
    0x00302080: "REG_VOL_PB",
    0x00302084: "REG_VOL_SOUND",
    0x00302088: "REG_SOUND",
    0x0030208C: "REG_PLAY",
    0x00302090: "REG_GPIO_DIR",
    0x00302094: "REG_GPIO",
    0x00302098: "REG_GPIOX_DIR",
    0x0030209C: "REG_GPIOX",
    0x003020A8: "REG_INT_FLAGS",
    0x003020AC: "REG_INT_EN",
    0x003020B0: "REG_INT_MASK",
    0x003020B4: "REG_PLAYBACK_START",
    0x003020B8: "REG_PLAYBACK_LENGTH",
    0x003020BC: "REG_PLAYBACK_READPTR",
    0x003020C0: "REG_PLAYBACK_FREQ",
    0x003020C4: "REG_PLAYBACK_FORMAT",
    0x003020C8: "REG_PLAYBACK_LOOP",
    0x003020CC: "REG_PLAYBACK_PLAY",
    0x003020D0: "REG_PWM_HZ",
    0x003020D4: "REG_PWM_DUTY",
    0x003020D8: "REG_MACRO_0",
    0x003020DC: "REG_MACRO_1",
    0x003020F8: "REG_CMD_READ",
    0x003020FC: "REG_CMD_WRITE",
    0x00302100: "REG_CMD_DL",
    0x00302104: "REG_TOUCH_MODE",
    0x00302108: "REG_TOUCH_ADC_MODE",
    0x0030210C: "REG_TOUCH_CHARGE",
    0x00302110: "REG_TOUCH_SETTLE",
    0x00302114: "REG_TOUCH_OVERSAMPLE",
    0x00302118: "REG_TOUCH_RZTHRESH",
    0x0030211C: "REG_TOUCH_RAW_XY",
    0x00302120: "REG_TOUCH_RZ",
    0x00302124: "REG_TOUCH_SCREEN_XY",
    0x00302128: "REG_TOUCH_TAG_XY",
    0x0030212C: "REG_TOUCH_TAG",
    0x00302130: "REG_TOUCH_TAG1_XY",
    0x00302134: "REG_TOUCH_TAG1",
    0x00302138: "REG_TOUCH_TAG2_XY",
    0x0030213C: "REG_TOUCH_TAG2",
    0x00302140: "REG_TOUCH_TAG3_XY",
    0x00302144: "REG_TOUCH_TAG3",
    0x00302148: "REG_TOUCH_TAG4_XY",
    0x0030214C: "REG_TOUCH_TAG4",
    0x00302150: "REG_TOUCH_TRANSFORM_A",
    0x00302154: "REG_TOUCH_TRANSFORM_B",
    0x00302158: "REG_TOUCH_TRANSFORM_C",
    0x0030215C: "REG_TOUCH_TRANSFORM_D",
    0x00302160: "REG_TOUCH_TRANSFORM_E",
    0x00302164: "REG_TOUCH_TRANSFORM_F",
    0x00302168: "REG_TOUCH_CONFIG",
    0x0030216C: "REG_CTOUCH_TOUCH4_X",
    0x00302174: "REG_BIST_EN",
    0x00302180: "REG_TRIM",
    0x00302184: "REG_ANA_COMP",
    0x00302188: "REG_SPI_WIDTH",
    0x0030218C: "REG_TOUCH_DIRECT_XY",
    0x00302190: "REG_TOUCH_DIRECT_Z1Z2",
    0x00302564: "REG_DATESTAMP",
    0x00302574: "REG_CMDB_SPACE",
    0x00302578: "REG_CMDB_WRITE",
    0x0030257C: "REG_ADAPTIVE_FRAMERATE",
    0x003025EC: "REG_PLAYBACK_PAUSE",
    0x003025F0: "REG_FLASH_STATUS",
    0x0030260C: "REG_UNDERRUN",
    0x00302610: "REG_AH_HCYCLE_MAX",
    0x00302614: "REG_PCLK_FREQ",
    0x00302618: "REG_PCLK_2X",
    0x00309000: "REG_TRACKER",
    0x00309004: "REG_TRACKER_1",
    0x00309008: "REG_TRACKER_2",
    0x0030900C: "REG_TRACKER_3",
    0x00309010: "REG_TRACKER_4",
    0x00309014: "REG_MEDIAFIFO_READ",
    0x00309018: "REG_MEDIAFIFO_WRITE",
    0x00309024: "REG_FLASH_SIZE",
    0x0030902C: "REG_ANIM_ACTIVE",
    0x0030914E: "REG_PLAY_CONTROL",
    0x00309162: "REG_COPRO_PATCH_PTR",
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
}

COPRO_COMMANDS = {
    0xFFFFFF1E: "CMD_APPEND",
    0xFFFFFF09: "CMD_BGCOLOR",
    0xFFFFFF0D: "CMD_BUTTON",
    0xFFFFFF15: "CMD_CALIBRATE",
    0xFFFFFF14: "CMD_CLOCK",
    0xFFFFFF32: "CMD_COLDSTART",
    0xFFFFFF2D: "CMD_DIAL",
    0xFFFFFF00: "CMD_DLSTART",
    0xFFFFFF0A: "CMD_FGCOLOR",
    0xFFFFFF13: "CMD_GAUGE",
    0xFFFFFF33: "CMD_GETMATRIX",
    0xFFFFFF25: "CMD_GETPROPS",
    0xFFFFFF23: "CMD_GETPTR",
    0xFFFFFF34: "CMD_GRADCOLOR",
    0xFFFFFF0B: "CMD_GRADIENT",
    0xFFFFFF22: "CMD_INFLATE",
    0xFFFFFF02: "CMD_INTERRUPT",
    0xFFFFFF0E: "CMD_KEYS",
    0xFFFFFF26: "CMD_LOADIDENTITY",
    0xFFFFFF24: "CMD_LOADIMAGE",
    0xFFFFFF31: "CMD_LOGO",
    0xFFFFFF39: "CMD_MEDIAFIFO",
    0xFFFFFF1D: "CMD_MEMCPY",
    0xFFFFFF18: "CMD_MEMCRC",
    0xFFFFFF1B: "CMD_MEMSET",
    0xFFFFFF1A: "CMD_MEMWRITE",
    0xFFFFFF1C: "CMD_MEMZERO",
    0xFFFFFF2E: "CMD_NUMBER",
    0xFFFFFF3A: "CMD_PLAYVIDEO",
    0xFFFFFF0F: "CMD_PROGRESS",
    0xFFFFFF19: "CMD_REGREAD",
    0xFFFFFF3F: "CMD_ROMFONT",
    0xFFFFFF29: "CMD_ROTATE",
    0xFFFFFF28: "CMD_SCALE",
    0xFFFFFF2F: "CMD_SCREENSAVER",
    0xFFFFFF11: "CMD_SCROLLBAR",
    0xFFFFFF38: "CMD_SETBASE",
    0xFFFFFF43: "CMD_SETBITMAP",
    0xFFFFFF2B: "CMD_SETFONT",
    0xFFFFFF3B: "CMD_SETFONT2",
    0xFFFFFF2A: "CMD_SETMATRIX",
    0xFFFFFF36: "CMD_SETROTATE",
    0xFFFFFF3C: "CMD_SETSCRATCH",
    0xFFFFFF30: "CMD_SKETCH",
    0xFFFFFF10: "CMD_SLIDER",
    0xFFFFFF1F: "CMD_SNAPSHOT",
    0xFFFFFF37: "CMD_SNAPSHOT2",
    0xFFFFFF16: "CMD_SPINNER",
    0xFFFFFF17: "CMD_STOP",
    0xFFFFFF01: "CMD_SWAP",
    0xFFFFFF42: "CMD_SYNC",
    0xFFFFFF0C: "CMD_TEXT",
    0xFFFFFF12: "CMD_TOGGLE",
    0xFFFFFF2C: "CMD_TRACK",
    0xFFFFFF27: "CMD_TRANSLATE",
    0xFFFFFF41: "CMD_VIDEOFRAME",
    0xFFFFFF40: "CMD_VIDEOSTART",
    0xFFFFFF21: "CMD_BITMAP_TRANSFORM",
    0xFFFFFF44: "CMD_FLASHERASE",
    0xFFFFFF45: "CMD_FLASHWRITE",
    0xFFFFFF46: "CMD_FLASHREAD",
    0xFFFFFF47: "CMD_FLASHUPDATE",
    0xFFFFFF48: "CMD_FLASHDETACH",
    0xFFFFFF49: "CMD_FLASHATTACH",
    0xFFFFFF4A: "CMD_FLASHFAST",
    0xFFFFFF4B: "CMD_FLASHSPIDESEL",
    0xFFFFFF4C: "CMD_FLASHSPITX",
    0xFFFFFF4D: "CMD_FLASHSPIRX",
    0xFFFFFF4E: "CMD_FLASHSOURCE",
    0xFFFFFF4F: "CMD_CLEARCACHE",
    0xFFFFFF50: "CMD_INFLATE2",
    0xFFFFFF51: "CMD_ROTATEAROUND",
    0xFFFFFF52: "CMD_RESETFONTS",
    0xFFFFFF53: "CMD_ANIMSTART",
    0xFFFFFF54: "CMD_ANIMSTOP",
    0xFFFFFF55: "CMD_ANIMXY",
    0xFFFFFF56: "CMD_ANIMDRAW",
    0xFFFFFF57: "CMD_GRADIENTA",
    0xFFFFFF58: "CMD_FILLWIDTH",
    0xFFFFFF59: "CMD_APPENDF",
    0xFFFFFF5A: "CMD_ANIMFRAME",
    0xFFFFFF5F: "CMD_VIDEOSTARTF",
    0xFFFFFF6D: "CMD_ANIMFRAMERAM",
    0xFFFFFF6E: "CMD_ANIMSTARTRAM",
    0xFFFFFF63: "CMD_APILEVEL",
    0xFFFFFF60: "CMD_CALIBRATESUB",
    0xFFFFFF67: "CMD_CALLLIST",
    0xFFFFFF69: "CMD_ENDLIST",
    0xFFFFFF70: "CMD_FLASHPROGRAM",
    0xFFFFFF6B: "CMD_FONTCACHE",
    0xFFFFFF6C: "CMD_FONTCACHEQUERY",
    0xFFFFFF64: "CMD_GETIMAGE",
    0xFFFFFF62: "CMD_HSF",
    0xFFFFFF5E: "CMD_LINETIME",
    0xFFFFFF68: "CMD_NEWLIST",
    0xFFFFFF6A: "CMD_PCLKFREQ",
    0xFFFFFF66: "CMD_RETURN",
    0xFFFFFF6F: "CMD_RUNANIM",
    0xFFFFFF61: "CMD_TESTCARD",
    0xFFFFFF65: "CMD_WAIT"
}

def decode_read_response(miso_buffer):
    """
    Extracts up to 4 bytes of little-endian return data from MISO after the 3-byte header and dummy byte.
    Returns formatted hex string or None.
    """
    miso_bytes = [b for _, _, b in miso_buffer]

    if len(miso_bytes) <= 4:
        return None  # Not enough bytes (need 3 header + 1 dummy + at least 1 data)

    data_bytes = miso_bytes[4:]  # Skip 3-byte addr + dummy
    if not data_bytes:
        return None

    if len(data_bytes) > 4:
        data_bytes = data_bytes[:4]  # Only take max 4

    value = int.from_bytes(data_bytes, byteorder='little')
    return f"0x{value:0{len(data_bytes) * 2}X}"

def decode_write_data(mosi_buffer):
    """
    Extracts up to 4 bytes of little-endian write data from MOSI after the 3-byte header.
    Returns formatted hex string or None.
    """
    mosi_bytes = [b for _, _, b in mosi_buffer]

    if len(mosi_bytes) <= 3:
        return None  # No data bytes

    data_bytes = mosi_bytes[3:]  # Skip 3-byte header
    if not data_bytes:
        return None

    if len(data_bytes) > 4:
        data_bytes = data_bytes[:4]  # Max 4 bytes

    value = int.from_bytes(data_bytes, byteorder='little')
    return f"0x{value:0{len(data_bytes) * 2}X}"

class Hla(HighLevelAnalyzer):
    result_types = {
        'command': {'format': '{}'},
        'read': {'format': '{} from 0x{:06X} = 0x{:X}'},
        'write': {'format': '{} to 0x{:06X} = 0x{:X}'}
    }

    def __init__(self):
        self.frame_buffer_mosi = []
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
            if len(self.frame_buffer_mosi) < 3:
                return None  # Not enough for any known frame

            mosi_bytes = [b for (_, _, b) in self.frame_buffer_mosi]
            start_time = self.frame_start_time or self.frame_buffer_mosi[0][0]
            end_time = self.frame_buffer_mosi[-1][1]

            # --- HOST COMMAND FRAME (3 bytes total) ---
            if len(mosi_bytes) == 3:
                cmd = mosi_bytes[0]
                cmd_name = COMMANDS.get(cmd, f"UNKNOWN_CMD (0x{cmd:02X})")
                return AnalyzerFrame(cmd_name, start_time, end_time, {})

            # --- Read/Write frame (address = 3 bytes, then variable-length data) ---
            if len(mosi_bytes) >= 4:
                addr22 = (
                    ((mosi_bytes[0] & 0x3f) << 16) |
                    (mosi_bytes[1] << 8) |
                    mosi_bytes[2]
                )
                addr = 0x00000000 | addr22

                is_write = (mosi_bytes[0] & 0x80) != 0
                op = "WRITE" if (mosi_bytes[0] & 0x80) else "READ"

                # Resolve register label or dynamic RAM-DL offset
                if 0x300000 <= addr <= 0x301FFF:
                    offset = addr - 0x300000
                    label = f"RAM-DL+0x{offset:04X}"
                else:
                    label = REGISTERS.get(addr, f"0x{addr:08X}")

                text = f"{op} {label}"

                if is_write:
                    # WRITE Frame
                    value_str = decode_write_data(self.frame_buffer_mosi)

                    if len(value_str) == 10 and (label.startswith("RAM-DL+0x") or label == 'REG_CMDB_WRITE'):
                        value_int = int(value_str, 16)
                        cmd_name = COPRO_COMMANDS.get(value_int, value_str)

                        if cmd_name != value_str:
                            value_str = cmd_name
                        else:
                            cmd_key = value_int & 0xFF000000
                            cmd_name = DL_COMMANDS.get(cmd_key)

                            if cmd_name:
                                value_str = f"{cmd_name} + 0x{value_int & 0x00FFFFFF:06X}"

                            if mosi_bytes[6] & 0xC0 == 0x40:
                                value_str = f"'DL_VERTEX2F' + 0x{value_int & 0x3FFFFFFF:08X}"

                            if mosi_bytes[6] & 0xC0 == 0x80:
                                value_str = f"'DL_VERTEX2II' + 0x{value_int & 0x3FFFFFFF:08X}"

                    return AnalyzerFrame(text, start_time, end_time, {
                        "data": value_str
                    })

                else:
                    # READ Frame
                    if len(self.frame_buffer_mosi) < 5:
                        return None  # Need at least dummy + 1 return byte

                    value_str = decode_read_response(self.frame_buffer_miso)

                    return AnalyzerFrame(text, start_time, end_time, {
                        "data": value_str or "READ_ERROR"
                    })

            return None
