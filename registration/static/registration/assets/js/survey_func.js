// JS OBUSCATED ONLY IN THE DEMO TO AVOID STEALING. DOWNLOADABLE FILE HAVE JS NOT ENCRYPTED
var _0x7647 = ["use strict", "action", "/event-registration/register/", "attr", "form#wrapped", ":radio", "is", ":checkbox", "next", "insertBefore", "insertAfter", "validate", "#wrapped", ".submit", "length", "val", "input#website", "isMovingForward", ":input", "find", "step", "state", "wizard", "valid", "#wizard_container", "progressbar", "#progressbar", "value", "percentComplete", "(", "stepsComplete", "/", "stepsPossible", ")", "text", "#location", "select:hidden", ".nice-select", "#question_1", "question_1", "name", ":checked", "push", "each", "input[name*='", "']", ", ", "join", "#question_2", "question_2", "#question_3", "question_3", "#additional_message", "additional_message"];
jQuery(function (_0xb44ax1) {
  _0x7647[0];
  _0xb44ax1(_0x7647[4])[_0x7647[3]](_0x7647[1], _0x7647[2]);
  _0xb44ax1(_0x7647[24])[_0x7647[22]]({
    stepsWrapper: _0x7647[12],
    submit: _0x7647[13],
    beforeSelect: function (_0xb44ax4, _0xb44ax5) {
      if (_0xb44ax1(_0x7647[16])[_0x7647[15]]()[_0x7647[14]] != 0) {
        return false;
      }
      ;
      if (!_0xb44ax5[_0x7647[17]]) {
        return true;
      }
      ;
      var _0xb44ax6 = _0xb44ax1(this)[_0x7647[22]](_0x7647[21])[_0x7647[20]][_0x7647[19]](_0x7647[18]);
      return !_0xb44ax6[_0x7647[14]] || !!_0xb44ax6[_0x7647[23]]();
    }
  })[_0x7647[11]]({
    errorPlacement: function (_0xb44ax2, _0xb44ax3) {
      if (_0xb44ax3[_0x7647[6]](_0x7647[5]) || _0xb44ax3[_0x7647[6]](_0x7647[7])) {
        _0xb44ax2[_0x7647[9]](_0xb44ax3[_0x7647[8]]());
      } else {
        _0xb44ax2[_0x7647[10]](_0xb44ax3);
      }
    }
  });
  _0xb44ax1(_0x7647[26])[_0x7647[25]]();
  _0xb44ax1(_0x7647[24])[_0x7647[22]]({
    afterSelect: function (_0xb44ax4, _0xb44ax5) {
      _0xb44ax1(_0x7647[26])[_0x7647[25]](_0x7647[27], _0xb44ax5[_0x7647[28]]);
      _0xb44ax1(_0x7647[35])[_0x7647[34]](_0x7647[29] + _0xb44ax5[_0x7647[30]] + _0x7647[31] + _0xb44ax5[_0x7647[32]] + _0x7647[33]);
    }
  });
  _0xb44ax1(_0x7647[12])[_0x7647[11]]({
    ignore: [],
    rules: {
      select: {
        required: true
      }
    },
    errorPlacement: function (_0xb44ax2, _0xb44ax3) {
      if (_0xb44ax3[_0x7647[6]](_0x7647[36])) {
        _0xb44ax2[_0x7647[10]](_0xb44ax3[_0x7647[8]](_0x7647[37]));
      } else {
        _0xb44ax2[_0x7647[10]](_0xb44ax3);
      }
    }
  });
});
function getVals(_0xb44ax8, _0xb44ax9) {
  switch (_0xb44ax9) {
    case _0x7647[39]:
      var _0xb44axa = $(_0xb44ax8)[_0x7647[15]]();
      $(_0x7647[38])[_0x7647[34]](_0xb44axa);
      break;
    case _0x7647[49]:
      var _0xb44axb = $(_0xb44ax8)[_0x7647[3]](_0x7647[40]);
      var _0xb44axa = [];
      $(_0x7647[44] + _0xb44axb + _0x7647[45])[_0x7647[43]](function () {
        if (jQuery(this)[_0x7647[6]](_0x7647[41])) {
          _0xb44axa[_0x7647[42]]($(this)[_0x7647[15]]());
        }
      });
      $(_0x7647[48])[_0x7647[34]](_0xb44axa[_0x7647[47]](_0x7647[46]));
      break;
    case _0x7647[51]:
      var _0xb44axa = $(_0xb44ax8)[_0x7647[15]]();
      $(_0x7647[50])[_0x7647[34]](_0xb44axa);
      break;
    case _0x7647[53]:
      var _0xb44axa = $(_0xb44ax8)[_0x7647[15]]();
      $(_0x7647[52])[_0x7647[34]](_0xb44axa);
      break;
  }
}