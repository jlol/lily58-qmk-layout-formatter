import sys
import parser

'''
    [LAYER_DEFAULT] = LAYOUT(
        KC_EQL,   KC_1,     KC_2,     KC_3,     KC_4,     KC_5,                         KC_6,     KC_7,     KC_8,     KC_9,     KC_0,     KC_MINS,
        KC_TAB,   KC_Q,     KC_W,     KC_E,     KC_R,     KC_T,                         KC_Y,     KC_U,     KC_I,     KC_O,     KC_P,     KC_BSPC,
        KC_ESC,   KC_A,     KC_S,     KC_D,     KC_F,     KC_G,                         KC_H,     KC_J,     KC_K,     KC_L,     KC_SCLN,  KC_QUOT,
        KC_LSFT,  KC_Z,     KC_X,     KC_C,     KC_V,     KC_B,     KC_WBAK,  KC_WFWD,  KC_N,     KC_M,     KC_COMM,  KC_DOT,   KC_SLSH,  KC_RSFT,
                                      KC_LALT,  KC_LCTL,  LY_LWR,   KC_SPC,   KC_ENT,   LY_RSE,   KC_RALT,  KC_RGUI
    ),
'''


all_input = ""

for line in sys.stdin:
    all_input += line

layers = parser.process_input(all_input)
