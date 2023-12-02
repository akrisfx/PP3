import re

# HTML код для тестирования
html_code = '''
<html>
<head>
    <title>Test Page</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js"></script>
</head>
<body>
    <a href="page.html">Link to HTML page</a>
    <img src="image.jpg" alt="Image">
</body>
</html>
'''

html2_code = '''
<!DOCTYPE html>

<html  dir="ltr" lang="ru" xml:lang="ru" data-dockeditem-title="2">
<head>
    <title>Прикл. прогр. (090303++): Лабораторная работа № 3 «Регулярные выражения. Работа с Git»</title>
    <link rel="shortcut icon" href="https://edu.stankin.ru/theme/opentechnology/pix/favicon.ico"/>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="moodle, Прикл. прогр. (090303++): Лабораторная работа № 3 «Регулярные выражения. Работа с Git»" />
<link rel="stylesheet" type="text/css" href="https://edu.stankin.ru/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.css" /><script id="firstthemesheet" type="text/css">/** Required in order to fix style inclusion problems in IE with YUI **/</script><link rel="stylesheet" type="text/css" href="https://edu.stankin.ru/theme/opentechnology/stylesprofile.php/profile/stankinc/1701486024/1/1697794360/1" />
<link rel="stylesheet" type="text/css" href="https://edu.stankin.ru/lib/editor/atto/plugins/otiframe/otiframe.css" />
<link rel="stylesheet" type="text/css" href="https://edu.stankin.ru/lib/editor/atto/plugins/otmagnifier/magnifier.css?v=1" />
<script>
//<![CDATA[
var M = {}; M.yui = {};
M.pageloadstarttime = new Date();
M.cfg = {"wwwroot":"https:\/\/edu.stankin.ru","homeurl":{},"sesskey":"0ldtSfBaXr","sessiontimeout":"7200","sessiontimeoutwarning":1200,"themerev":"1701486024","slasharguments":1,"theme":"opentechnology","iconsystemmodule":"core\/icon_system_fontawesome","jsrev":"1701486024","admin":"admin","svgicons":true,"usertimezone":"\u0415\u0432\u0440\u043e\u043f\u0430\/\u041c\u043e\u0441\u043a\u0432\u0430","courseId":11060,"courseContextId":188242,"contextid":659204,"contextInstanceId":380903,"langrev":1701486024,"templaterev":"1701486024"};var yui1ConfigFn = function(me) {if(/-skin|reset|fonts|grids|base/.test(me.name)){me.type='css';me.path=me.path.replace(/\.js/,'.css');me.path=me.path.replace(/\/yui2-skin/,'/assets/skins/sam/yui2-skin')}};
var yui2ConfigFn = function(me) {var parts=me.name.replace(/^moodle-/,'').split('-'),component=parts.shift(),module=parts[0],min='-min';if(/-(skin|core)$/.test(me.name)){parts.pop();me.type='css';min=''}
if(module){var filename=parts.join('-');me.path=component+'/'+module+'/'+filename+min+'.'+me.type}else{me.path=component+'/'+component+'.'+me.type}};
YUI_config = {"debug":false,"base":"https:\/\/edu.stankin.ru\/lib\/yuilib\/3.17.2\/","comboBase":"https:\/\/edu.stankin.ru\/theme\/yui_combo.php?","combine":true,"filter":null,"insertBefore":"firstthemesheet","groups":{"yui2":{"base":"https:\/\/edu.stankin.ru\/lib\/yuilib\/2in3\/2.9.0\/build\/","comboBase":"https:\/\/edu.stankin.ru\/theme\/yui_combo.php?","combine":true,"ext":false,"root":"2in3\/2.9.0\/build\/","patterns":{"yui2-":{"group":"yui2","configFn":yui1ConfigFn}}},"moodle":{"name":"moodle","base":"https:\/\/edu.stankin.ru\/theme\/yui_combo.php?m\/1701486024\/","combine":true,"comboBase":"https:\/\/edu.stankin.ru\/theme\/yui_combo.php?","ext":false,"root":"m\/1701486024\/","patterns":{"moodle-":{"group":"moodle","configFn":yui2ConfigFn}},"filter":null,"modules":{"moodle-core-handlebars":{"condition":{"trigger":"handlebars","when":"after"}},"moodle-core-event":{"requires":["event-custom"]},"moodle-core-languninstallconfirm":{"requires":["base","node","moodle-core-notification-confirm","moodle-core-notification-alert"]},"moodle-core-formchangechecker":{"requires":["base","event-focus","moodle-core-event"]},"moodle-core-blocks":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification"]},"moodle-core-chooserdialogue":{"requires":["base","panel","moodle-core-notification"]},"moodle-core-popuphelp":{"requires":["moodle-core-tooltip"]},"moodle-core-maintenancemodetimer":{"requires":["base","node"]},"moodle-core-notification":{"requires":["moodle-core-notification-dialogue","moodle-core-notification-alert","moodle-core-notification-confirm","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-core-notification-dialogue":{"requires":["base","node","panel","escape","event-key","dd-plugin","moodle-core-widget-focusafterclose","moodle-core-lockscroll"]},"moodle-core-notification-alert":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-confirm":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-exception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-ajaxexception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-actionmenu":{"requires":["base","event","node-event-simulate"]},"moodle-core-lockscroll":{"requires":["plugin","base-build"]},"moodle-core-tooltip":{"requires":["base","node","io-base","moodle-core-notification-dialogue","json-parse","widget-position","widget-position-align","event-outside","cache-base"]},"moodle-core-dragdrop":{"requires":["base","node","io","dom","dd","event-key","event-focus","moodle-core-notification"]},"moodle-core_availability-form":{"requires":["base","node","event","event-delegate","panel","moodle-core-notification-dialogue","json"]},"moodle-backup-backupselectall":{"requires":["node","event","node-event-simulate","anim"]},"moodle-backup-confirmcancel":{"requires":["node","node-event-simulate","moodle-core-notification-confirm"]},"moodle-course-util":{"requires":["node"],"use":["moodle-course-util-base"],"submodules":{"moodle-course-util-base":{},"moodle-course-util-section":{"requires":["node","moodle-course-util-base"]},"moodle-course-util-cm":{"requires":["node","moodle-course-util-base"]}}},"moodle-course-management":{"requires":["base","node","io-base","moodle-core-notification-exception","json-parse","dd-constrain","dd-proxy","dd-drop","dd-delegate","node-event-delegate"]},"moodle-course-categoryexpander":{"requires":["node","event-key"]},"moodle-course-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-course-coursebase","moodle-course-util"]},"moodle-form-passwordunmask":{"requires":[]},"moodle-form-dateselector":{"requires":["base","node","overlay","calendar"]},"moodle-form-shortforms":{"requires":["node","base","selector-css3","moodle-core-event"]},"moodle-question-preview":{"requires":["base","dom","event-delegate","event-key","core_question_engine"]},"moodle-question-chooser":{"requires":["moodle-core-chooserdialogue"]},"moodle-question-searchform":{"requires":["base","node"]},"moodle-availability_active-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_assignfeedback-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_badge-form":{"requires":["base","node","event","moodle-core_badge-form"]},"moodle-availability_completion-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_counter-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_coursecompleted-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_date-form":{"requires":["base","node","event","io","moodle-core_availability-form"]},"moodle-availability_duration-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_examus-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_examus2-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_grade-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_group-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_grouping-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_language-form":{"requires":["base","node","event","node-event-simulate","moodle-core_availability-form"]},"moodle-availability_otcomparison-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_othercompleted-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_password-popup":{"requires":["base","node","event","moodle-core-notification-dialogue","io-base"]},"moodle-availability_password-form":{"requires":["base","node","event","event-valuechange","moodle-core_availability-form"]},"moodle-availability_profile-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_role-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_xp-form":{"requires":["base","node","event","handlebars","moodle-core_availability-form"]},"moodle-mod_assign-history":{"requires":["node","transition"]},"moodle-mod_checklist-linkselect":{"requires":["node","event-valuechange"]},"moodle-mod_offlinequiz-offlinequizbase":{"requires":["base","node"]},"moodle-mod_offlinequiz-repaginate":{"requires":["base","event","node","io","moodle-core-notification-dialogue"]},"moodle-mod_offlinequiz-toolboxes":{"requires":["base","node","event","event-key","io","moodle-mod_offlinequiz-offlinequizbase","moodle-mod_offlinequiz-util-slot","moodle-core-notification-ajaxexception"]},"moodle-mod_offlinequiz-util":{"requires":["node"],"use":["moodle-mod_offlinequiz-util-base"],"submodules":{"moodle-mod_offlinequiz-util-base":{},"moodle-mod_offlinequiz-util-slot":{"requires":["node","moodle-mod_offlinequiz-util-base"]},"moodle-mod_offlinequiz-util-page":{"requires":["node","moodle-mod_offlinequiz-util-base"]}}},"moodle-mod_offlinequiz-modform":{"requires":["base","node","event"]},"moodle-mod_offlinequiz-questionchooser":{"requires":["moodle-core-chooserdialogue","moodle-mod_offlinequiz-util","querystring-parse"]},"moodle-mod_offlinequiz-randomquestion":{"requires":["base","event","node","io","moodle-core-notification-dialogue"]},"moodle-mod_offlinequiz-autosave":{"requires":["base","node","event","event-valuechange","node-event-delegate","io-form"]},"moodle-mod_offlinequiz-offlinequizquestionbank":{"requires":["base","event","node","io","io-form","yui-later","moodle-question-qbankmanager","moodle-qbank_editquestion-chooser","moodle-question-searchform","moodle-core-notification"]},"moodle-mod_offlinequiz-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-mod_offlinequiz-offlinequizbase","moodle-mod_offlinequiz-util-base","moodle-mod_offlinequiz-util-page","moodle-mod_offlinequiz-util-slot","moodle-course-util"]},"moodle-mod_quiz-toolboxes":{"requires":["base","node","event","event-key","io","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-slot","moodle-core-notification-ajaxexception"]},"moodle-mod_quiz-util":{"requires":["node","moodle-core-actionmenu"],"use":["moodle-mod_quiz-util-base"],"submodules":{"moodle-mod_quiz-util-base":{},"moodle-mod_quiz-util-slot":{"requires":["node","moodle-mod_quiz-util-base"]},"moodle-mod_quiz-util-page":{"requires":["node","moodle-mod_quiz-util-base"]}}},"moodle-mod_quiz-modform":{"requires":["base","node","event"]},"moodle-mod_quiz-questionchooser":{"requires":["moodle-core-chooserdialogue","moodle-mod_quiz-util","querystring-parse"]},"moodle-mod_quiz-autosave":{"requires":["base","node","event","event-valuechange","node-event-delegate","io-form"]},"moodle-mod_quiz-quizbase":{"requires":["base","node"]},"moodle-mod_quiz-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-base","moodle-mod_quiz-util-page","moodle-mod_quiz-util-slot","moodle-course-util"]},"moodle-mod_scheduler-delselected":{"requires":["base","node","event"]},"moodle-mod_scheduler-saveseen":{"requires":["base","node","event"]},"moodle-mod_scheduler-studentlist":{"requires":["base","node","event","io"]},"moodle-message_airnotifier-toolboxes":{"requires":["base","node","io"]},"moodle-block_xp-rulepicker":{"requires":["base","node","handlebars","moodle-core-notification-dialogue"]},"moodle-block_xp-notification":{"requires":["base","node","handlebars","button-plugin","moodle-core-notification-dialogue"]},"moodle-block_xp-filters":{"requires":["base","node","moodle-core-dragdrop","moodle-core-notification-confirm","moodle-block_xp-rulepicker"]},"moodle-filter_glossary-autolinker":{"requires":["base","node","io-base","json-parse","event-delegate","overlay","moodle-core-event","moodle-core-notification-alert","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-filter_mathjaxloader-loader":{"requires":["moodle-core-event"]},"moodle-editor_atto-rangy":{"requires":[]},"moodle-editor_atto-editor":{"requires":["node","transition","io","overlay","escape","event","event-simulate","event-custom","node-event-html5","node-event-simulate","yui-throttle","moodle-core-notification-dialogue","moodle-core-notification-confirm","moodle-editor_atto-rangy","handlebars","timers","querystring-stringify"]},"moodle-editor_atto-plugin":{"requires":["node","base","escape","event","event-outside","handlebars","event-custom","timers","moodle-editor_atto-menu"]},"moodle-editor_atto-menu":{"requires":["moodle-core-notification-dialogue","node","event","event-custom"]},"moodle-report_eventlist-eventfilter":{"requires":["base","event","node","node-event-delegate","datatable","autocomplete","autocomplete-filters"]},"moodle-report_loglive-fetchlogs":{"requires":["base","event","node","io","node-event-delegate"]},"moodle-report_overviewstats-charts":{"requires":["base","node","charts","charts-legend"]},"moodle-gradereport_history-userselector":{"requires":["escape","event-delegate","event-key","handlebars","io-base","json-parse","moodle-core-notification-dialogue"]},"moodle-qbank_editquestion-chooser":{"requires":["moodle-core-chooserdialogue"]},"moodle-tool_capability-search":{"requires":["base","node"]},"moodle-tool_lp-dragdrop-reorder":{"requires":["moodle-core-dragdrop"]},"moodle-tool_monitor-dropdown":{"requires":["base","event","node"]},"moodle-assignfeedback_editpdf-editor":{"requires":["base","event","node","io","graphics","json","event-move","event-resize","transition","querystring-stringify-simple","moodle-core-notification-dialog","moodle-core-notification-alert","moodle-core-notification-warning","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-atto_accessibilitychecker-button":{"requires":["color-base","moodle-editor_atto-plugin"]},"moodle-atto_accessibilityhelper-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_align-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_bold-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_c4l-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_charmap-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_clear-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_collapse-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_emojipicker-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_emoticon-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_equation-button":{"requires":["moodle-editor_atto-plugin","moodle-core-event","io","event-valuechange","tabview","array-extras"]},"moodle-atto_fullscreen-button":{"requires":["event-resize","moodle-editor_atto-plugin"]},"moodle-atto_h5p-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_html-beautify":{},"moodle-atto_html-button":{"requires":["promise","moodle-editor_atto-plugin","moodle-atto_html-beautify","moodle-atto_html-codemirror","event-valuechange"]},"moodle-atto_html-codemirror":{"requires":["moodle-atto_html-codemirror-skin"]},"moodle-atto_htmlplus-beautify":{},"moodle-atto_htmlplus-button":{"requires":["moodle-editor_atto-plugin","moodle-atto_htmlplus-beautify","moodle-atto_htmlplus-codemirror","event-valuechange"]},"moodle-atto_htmlplus-codemirror":{"requires":["moodle-atto_htmlplus-codemirror-skin"]},"moodle-atto_image-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_indent-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_italic-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_link-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-usedfiles":{"requires":["node","escape"]},"moodle-atto_media-button":{"requires":["moodle-editor_atto-plugin","moodle-form-shortforms"]},"moodle-atto_noautolink-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_orderedlist-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_otiframe-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_otspoiler-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_recordrtc-recording":{"requires":["moodle-atto_recordrtc-button"]},"moodle-atto_recordrtc-button":{"requires":["moodle-editor_atto-plugin","moodle-atto_recordrtc-recording"]},"moodle-atto_rtl-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_strike-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_styles-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_subscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_superscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_table-button":{"requires":["moodle-editor_atto-plugin","moodle-editor_atto-menu","event","event-valuechange"]},"moodle-atto_textjustify-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_title-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_underline-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_undo-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_unorderedlist-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_wiris-button":{"requires":["moodle-editor_atto-plugin","get"]},"moodle-atto_wordimport-button":{"requires":["moodle-editor_atto-plugin"]}}},"gallery":{"name":"gallery","base":"https:\/\/edu.stankin.ru\/lib\/yuilib\/gallery\/","combine":true,"comboBase":"https:\/\/edu.stankin.ru\/theme\/yui_combo.php?","ext":false,"root":"gallery\/1701486024\/","patterns":{"gallery-":{"group":"gallery"}}}},"modules":{"core_filepicker":{"name":"core_filepicker","fullpath":"https:\/\/edu.stankin.ru\/lib\/javascript.php\/1701486024\/repository\/filepicker.js","requires":["base","node","node-event-simulate","json","async-queue","io-base","io-upload-iframe","io-form","yui2-treeview","panel","cookie","datatable","datatable-sort","resize-plugin","dd-plugin","escape","moodle-core_filepicker","moodle-core-notification-dialogue"]},"core_comment":{"name":"core_comment","fullpath":"https:\/\/edu.stankin.ru\/lib\/javascript.php\/1701486024\/comment\/comment.js","requires":["base","io-base","node","json","yui2-animation","overlay","escape"]},"mathjax":{"name":"mathjax","fullpath":"https:\/\/cdn.jsdelivr.net\/npm\/mathjax@2.7.9\/MathJax.js?delayStartupUntil=configured"}}};
M.yui.loader = {modules: {}};

//]]>
</script>

    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
</head>
<body  id="page-mod-assign-view" class="format-topics limitedwidth  path-mod path-mod-assign chrome dir-ltr lang-ru yui-skin-sam yui3-skin-sam edu-stankin-ru pagelayout-incourse course-11060 context-659204 cmid-380903 cm-type-assign category-445 theme-ot profile_stankinc uses-drawers">
<div id="body-inner" class="">

<div>
    <a class="sr-only sr-only-focusable" href="#maincontent">Перейти к основному содержанию</a>
</div><script src="https://edu.stankin.ru/lib/javascript.php/1701486024/lib/polyfills/polyfill.js"></script>
<script src="https://edu.stankin.ru/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.js"></script><script src="https://edu.stankin.ru/theme/jquery.php/core/jquery-3.6.1.min.js"></script>
<script src="https://edu.stankin.ru/lib/javascript.php/1701486024/lib/javascript-static.js"></script>
<script>
//<![CDATA[
document.body.className += ' jsenabled';
//]]>
</script>

<script>var u=localStorage.getItem('otLoginWantsUrl');if(u){localStorage.removeItem('otLoginWantsUrl');localStorage.removeItem('otJustRegistered');document.location.href=decodeURI(u)}</script><header id="page-header" class="hide-empty-dock dock-has-items">


	<div class="wrapper">
        <div id="h_top_wrapper" class="h_top_wrapper container-fluid  ">

            <div id="h_top" class="h_top flex-column flex-lg-row align-items-center align-items-md-stretch  justify-content-center justify-content-lg-between " data-primary-x="right" data-primary-y="bottom" data-has-header-text="1">
               	<div id="h_leftblock_wrapper" class="h_leftblock_wrapper align-items-center align-items-md-stretch justify-content-center justify-content-md-start">

           			<div class="header_logoimage_wrappper flex-column align-items-center align-items-md-start flex-md-row"><a class="header_logoimage mr-0 mr-md-2" href="https://edu.stankin.ru/"><img class="logo" src="//edu.stankin.ru/pluginfile.php/1/theme_opentechnology/settings_stankinc_header_logoimage/1701486024/Z3%20%284%29.png" alt="В начало" /><img class="compact-logo" src="//edu.stankin.ru/pluginfile.php/1/theme_opentechnology/settings_stankinc_header_logoimage/1701486024/Z3%20%284%29.png" alt="В начало" /></a><div class="h_logo_title mr-0 mr-md-2 mt-2 mt-md-0 mb-1 mb-md-0"><div class="h_logo_title_text text-center text-md-left"><div><p><b><span class="" style="font-size: x-large;">Электронная&nbsp;образовательная&nbsp;среда</span></b></p>
<p><b><span class="" style="font-size: x-large;">ФГБОУ&nbsp;ВО&nbsp;«МГТУ&nbsp;«СТАНКИН»</span></b></p></div></div></div></div>


               	</div>
               	<div id="h_rightblock_wrapper" class="h_rightblock_wrapper  nocaret">

                   	<div class="usernav justify-content-center justify-content-md-start">




                   				<a class="btn btn-primary button_mycourses header_link" title="" data-toggle="tooltip" data-placement="bottom" href="https://edu.stankin.ru/my/courses.php" data-original-title="Мои курсы"></a>

                   		<div class="d-flex flex-wrap justify-content-end">
                   		<div class="usermenu moodle-has-zindex"><div class="action-menu moodle-actionmenu nowrap-items" id="action-menu-0" data-enhance="moodle-core-actionmenu">

        <div class="menubar d-flex " id="action-menu-0-menubar">




                <div class="action-menu-trigger">
                    <div class="dropdown">
                        <a
                            href="#"
                            tabindex="0"
                            class="toggle-display dropdown-toggle icon-no-margin"
                            id="action-menu-toggle-0"
                            aria-label="Потачин Владислав НиколаевичВП"
                            data-toggle="dropdown"
                            role="button"
                            aria-haspopup="true"
                            aria-expanded="false"
                            aria-controls="action-menu-0-menu"
                        >

                            <span class="userbutton"><span class="usertext">Потачин Владислав Николаевич</span><span class="avatars"><span class="avatar current"><span class="userinitials size-35">ВП</span></span></span></span>

                            <b class="caret"></b>
                        </a>
                            <div class="dropdown-menu menu dropdown-menu-right" id="action-menu-0-menu" data-rel="menu-content" aria-labelledby="action-menu-toggle-0" role="menu">
                                                                <a href="https://edu.stankin.ru/my/" class="dropdown-item userfullname text-truncate menu-action" role="menuitem" tabindex="-1" aria-labelledby="actionmenuaction-1">
                                <span class="menu-action-text" id="actionmenuaction-1">Личный кабинет</span>
                        </a>
                                                                <a href="https://edu.stankin.ru/user/profile.php" class="dropdown-item text-truncate menu-action" role="menuitem" data-title="profile,moodle" tabindex="-1" aria-labelledby="actionmenuaction-2">
                                <span class="menu-action-text" id="actionmenuaction-2">О пользователе</span>
                        </a>
                    <div class="dropdown-divider" role="presentation"><span class="filler">&nbsp;</span></div>
                                                                <a href="https://edu.stankin.ru/grade/report/overview/index.php" class="dropdown-item text-truncate menu-action" role="menuitem" data-title="grades,grades" tabindex="-1" aria-labelledby="actionmenuaction-3">
                                <span class="menu-action-text" id="actionmenuaction-3">Оценки</span>
                        </a>
                                                                <a href="https://edu.stankin.ru/calendar/view.php?view=month" class="dropdown-item text-truncate menu-action" role="menuitem" data-title="calendar,core_calendar" tabindex="-1" aria-labelledby="actionmenuaction-4">
                                <span class="menu-action-text" id="actionmenuaction-4">Календарь</span>
                        </a>
                                                                <a href="https://edu.stankin.ru/message/index.php" class="dropdown-item text-truncate menu-action" role="menuitem" data-title="messages,message" tabindex="-1" aria-labelledby="actionmenuaction-5">
                                <span class="menu-action-text" id="actionmenuaction-5">Сообщения</span>
                        </a>
                                                                <a href="https://edu.stankin.ru/user/files.php" class="dropdown-item text-truncate menu-action" role="menuitem" data-title="privatefiles,moodle" tabindex="-1" aria-labelledby="actionmenuaction-6">
                                <span class="menu-action-text" id="actionmenuaction-6">Личные файлы</span>
                        </a>
                                                                <a href="https://edu.stankin.ru/reportbuilder/index.php" class="dropdown-item text-truncate menu-action" role="menuitem" data-title="reports,core_reportbuilder" tabindex="-1" aria-labelledby="actionmenuaction-7">
                                <span class="menu-action-text" id="actionmenuaction-7">Отчеты</span>
                        </a>
                    <div class="dropdown-divider" role="presentation"><span class="filler">&nbsp;</span></div>
                                                                <a href="https://edu.stankin.ru/user/preferences.php" class="dropdown-item text-truncate menu-action" role="menuitem" data-title="preferences,moodle" tabindex="-1" aria-labelledby="actionmenuaction-8">
                                <span class="menu-action-text" id="actionmenuaction-8">Настройки</span>
                        </a>
                    <div class="dropdown-divider" role="presentation"><span class="filler">&nbsp;</span></div>
                                                                <a href="https://edu.stankin.ru/login/logout.php?sesskey=0ldtSfBaXr" class="dropdown-item text-truncate menu-action" role="menuitem" data-title="logout,moodle" tabindex="-1" aria-labelledby="actionmenuaction-9">
                                <span class="menu-action-text" id="actionmenuaction-9">Выход</span>
                        </a>
                            </div>
                    </div>
                </div>

        </div>

</div></div>
                   	   	<div class="navbar-nav"><div class="popover-region otsupport schrodinger" id="ot-support-navbar-656b0a6ba6517"></div><div class="popover-region collapsed popover-region-notifications position-left"
    id="nav-notification-popover-container" data-userid="24186" 
    data-region="popover-region">
    <div class="popover-region-toggle nav-link icon-no-margin"
        data-region="popover-region-toggle"
        role="button"
        aria-controls="popover-region-container-656b0a6ba53a3656b0a6ba1c2e59"
        aria-haspopup="true"
        aria-label="Показать окно без новых уведомлений"
        tabindex="0">
            	<div class="nav-link icon-no-margin" data-toggle="tooltip" data-placement="bottom" data-original-title="Уведомления"/>
        	<img class="icon " alt="" aria-hidden="true" src="https://edu.stankin.ru/theme/image.php/opentechnology/theme_opentechnology/1701486024/notifications" />
        </div>
        <div class="count-container hidden" data-region="count-container">0</div>

    </div>
    <div 
        id="popover-region-container-656b0a6ba53a3656b0a6ba1c2e59"
        class="popover-region-container"
        data-region="popover-region-container"
        aria-expanded="false"
        aria-hidden="true"
        aria-label="Окно уведомления"
        role="region">
        <div class="popover-region-header-container">
            <h3 class="popover-region-header-text" data-region="popover-region-header-text">Уведомления</h3>
            <div class="popover-region-header-actions" data-region="popover-region-header-actions">        <a class="mark-all-read-button"
           href="#"
           title="Пометить все прочитанным"
           data-action="mark-all-read"
           role="button">
            <span class="normal-icon"><i class="icon fa fa-check fa-fw "  title="Пометить все прочитанным" role="img" aria-label="Пометить все прочитанным"></i></span>
            <span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
        </a>
        <a href="https://edu.stankin.ru/message/notificationpreferences.php"
           title="Настройка уведомлений">
            <i class="icon fa fa-cog fa-fw "  title="Настройка уведомлений" role="img" aria-label="Настройка уведомлений"></i>
        </a>
</div>
        </div>
        <div class="popover-region-content-container" data-region="popover-region-content-container">
            <div class="popover-region-content" data-region="popover-region-content">
                        <div class="all-notifications"
            data-region="all-notifications"
            role="log"
            aria-busy="false"
            aria-atomic="false"
            aria-relevant="additions"></div>
        <div class="empty-message" tabindex="0" data-region="empty-message">Уведомлений нет</div>

            </div>
            <span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
        </div>
                <a class="see-all-link"
                    href="https://edu.stankin.ru/message/output/popup/notifications.php">
                    <div class="popover-region-footer-container">
                        <div class="popover-region-seeall-text">Смотреть все</div>
                    </div>
                </a>
    </div>
</div><div class="popover-region collapsed" data-region="popover-region-messages">
    <a id="message-drawer-toggle-656b0a6ba618e656b0a6ba1c2e60" class="nav-link popover-region-toggle position-relative icon-no-margin" href="#"
            role="button">
        <div class="nav-link icon-no-margin" data-toggle="tooltip" data-placement="bottom" data-original-title="Сообщения"/>
        	<img class="icon oticon" alt="" aria-hidden="true" src="https://edu.stankin.ru/theme/image.php/opentechnology/theme_opentechnology/1701486024/message" />
        </div>
        <div
            class="count-container hidden"
            data-region="count-container"
        >
            <span aria-hidden="true">0</span>
            <span class="sr-only">Непрочитанных бесед: 0</span>
        </div>
    </a>
    <span class="sr-only sr-only-focusable" data-region="jumpto" tabindex="-1"></span></div></div>
                   		</div>

                   	</div>
			        <div class="primary-navigation d-flex align-items-center">
			       		<nav class="moremenu navigation">
    <ul id="moremenu-656b0a6ba40c3-navbar-nav" role="menubar" class="nav more-nav navbar-nav">
                <li data-key="mycourses" class="nav-item" role="none" data-forceintomoremenu="false">
                            <a role="menuitem" class="nav-link  "
                                href="https://edu.stankin.ru/my/courses.php"

                                tabindex="-1"
                            >
                                Мои курсы
                            </a>
                </li>
                <li data-key="" class="nav-item" role="none" data-forceintomoremenu="false">
                            <a role="menuitem" class="nav-link  "
                                href="https://edu.stankin.ru/course/view.php?id=11551"

                                tabindex="-1"
                            >
                                Навигация по ЭОС
                            </a>
                </li>
        <li role="none" class="nav-item dropdown dropdownmoremenu d-none" data-region="morebutton">
            <a class="dropdown-toggle nav-link " href="#" id="moremenu-dropdown-656b0a6ba40c3" role="menuitem" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" tabindex="-1">
                Дополнительно
            </a>
            <ul class="dropdown-menu dropdown-menu-left" data-region="moredropdown" aria-labelledby="moremenu-dropdown-656b0a6ba40c3" role="menu">
            </ul>
        </li>
    </ul>
</nav>


			        	<div class="langmenu">
    <div class="dropdown show">
        <a href="#" role="button" id="lang-menu-toggle" data-toggle="dropdown" aria-label="Язык" aria-haspopup="true" aria-controls="lang-action-menu" class="btn dropdown-toggle">
            <i class="icon fa fa-language fa-fw mr-1" aria-hidden="true"></i>
            <span class="langbutton">
                Русский ‎(ru)‎
            </span>
            <b class="caret"></b>
        </a>
        <div role="menu" aria-labelledby="lang-menu-toggle" id="lang-action-menu" class="dropdown-menu dropdown-menu-right">
                    <a href="#" class="dropdown-item pl-5" role="menuitem" aria-current="true"
                            >
                        Русский ‎(ru)‎
                    </a>
                    <a href="https://edu.stankin.ru/mod/assign/view.php?id=380903&amp;rownum=0&amp;useridlistid=656b0a6b8be7f393768426&amp;action&amp;lang=en" class="dropdown-item pl-5" role="menuitem" 
                            lang="en" >
                        English ‎(en)‎
                    </a>
        </div>
    </div>
</div>

			        </div>

               	</div>
           	</div>

       	</div>
    </div>
    <div class="dock_bg_wrapper">
        <div id="dock_bg" class="container-fluid ">

       	</div>
   	</div>
</header><div class="drawer-toggles drawer-toggles-left d-flex">
    <div class="drawer-toggles-left">
        <div class="drawer-toggler drawer-left-toggle open-nav d-print-none drawer-toggler-breadcrumbs">
            <button
                class="btn icon-no-margin"
                data-toggler="drawers"
                data-action="toggle"
                data-target="theme_opentechnology-drawers-breadcrumbs"
                data-toggle="tooltip"
                data-placement="right"
                title="Открыть хлебные крошки"
            >
                <span class="fa-stack fa-lg icon icon-to-open"><i class="icon fa fa-ellipsis-h fa-fw " aria-hidden="true"  ></i></span>
                <span class="fa-stack fa-lg icon icon-to-close">
				  <i class="fa fa-home fa-stack-1x" style="margin-top: -3px;"></i>
				  <i class="fa fa-ellipsis-h fa-stack-1x " style="margin-top: 8px;"></i>
				</span>
            </button>
        </div>
        <div class="drawer-toggler drawer-left-toggle open-nav d-print-none drawer-toggler-courseindex">
            <button
                class="btn icon-no-margin"
                data-toggler="drawers"
                data-action="toggle"
                data-target="theme_opentechnology-drawers-courseindex"
                data-toggle="tooltip"
                data-placement="right"
                title="Открыть панель оглавления курса"
            >
                <span class="icon-to-open"><i class="icon fa fa-list fa-fw " aria-hidden="true"  ></i></span>
                <span class="icon-to-close"><i class="icon fa fa-times fa-fw " aria-hidden="true"  ></i></span>
            </button>
        </div>
    </div>
    <div class="drawer-toggles-right">
    </div>
</div>
<div class="drawers">
    <div  class="drawer drawer-left d-print-none not-initialized" data-region="fixed-drawer" id="theme_opentechnology-drawers-breadcrumbs" data-preference="" data-state="show-drawer-left" data-forceopen="0" data-close-on-resize="0">
    <div class="drawerheader">
        <button
            class="btn drawertoggle icon-no-margin hidden"
            data-toggler="drawers"
            data-action="closedrawer"
            data-target="theme_opentechnology-drawers-breadcrumbs"
            data-toggle="tooltip"
            data-placement="right"
            title="Закрыть панель"
        >
            <i class="icon fa fa-times fa-fw " aria-hidden="true"  ></i>
        </button>
    </div>
    <div class="drawercontent drag-container" data-usertour="scroller">
                    <span class="accesshide" id="navbar-label">Путь к странице</span><nav aria-labelledby="navbar-label"><ul class="breadcrumb"><li data-node-type="60" class=""><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a itemprop="url" href="https://edu.stankin.ru/"><span itemprop="title">В начало</span></a></span><span class="divider"> <span class="accesshide " ><span class="arrow_text">/</span>&nbsp;</span><span class="arrow sep">&#9658;</span> </span></li><li data-node-type="0" class=""><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a itemprop="url" href="https://edu.stankin.ru/my/courses.php"><span itemprop="title">Мои курсы</span></a></span><span class="divider"> <span class="accesshide " ><span class="arrow_text">/</span>&nbsp;</span><span class="arrow sep">&#9658;</span> </span></li><li data-node-type="11" class=""><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a itemprop="url" href="https://edu.stankin.ru/course/index.php?categoryid=446"><span itemprop="title">Бакалавриат (ФГОС 3++)</span></a></span><span class="divider"> <span class="accesshide " ><span class="arrow_text">/</span>&nbsp;</span><span class="arrow sep">&#9658;</span> </span></li><li data-node-type="11" class=""><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a itemprop="url" href="https://edu.stankin.ru/course/index.php?categoryid=440"><span itemprop="title">УГСН 09.00.00 (ФГОС 3++)</span></a></span><span class="divider"> <span class="accesshide " ><span class="arrow_text">/</span>&nbsp;</span><span class="arrow sep">&#9658;</span> </span></li><li data-node-type="11" class=""><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a itemprop="url" href="https://edu.stankin.ru/course/index.php?categoryid=445"><span itemprop="title">Общие дисциплины (09 группа)</span></a></span><span class="divider"> <span class="accesshide " ><span class="arrow_text">/</span>&nbsp;</span><span class="arrow sep">&#9658;</span> </span></li><li data-node-type="20" class="about_course"><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a itemprop="url" title="О курсе" href="https://edu.stankin.ru/local/crw/course.php?id=11060"><span itemprop="title">О курсе</span></a></span><span class="divider"> <span class="accesshide " ><span class="arrow_text">/</span>&nbsp;</span><span class="arrow sep">&#9658;</span> </span></li><li data-node-type="20" class=""><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a itemprop="url" title="Прикладное программирование" href="https://edu.stankin.ru/course/view.php?id=11060"><span itemprop="title">Прикл. прогр. (090303++)</span></a></span><span class="divider"> <span class="accesshide " ><span class="arrow_text">/</span>&nbsp;</span><span class="arrow sep">&#9658;</span> </span></li><li data-node-type="30" class=""><span tabindex="0">Лабораторные работы</span><span class="divider"> <span class="accesshide " ><span class="arrow_text">/</span>&nbsp;</span><span class="arrow sep">&#9658;</span> </span></li><li data-node-type="40" class="active_tree_node"><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a itemprop="url" title="Задание" aria-current="page" href="https://edu.stankin.ru/mod/assign/view.php?id=380903"><span itemprop="title">Лабораторная работа № 3 «Регулярные выражения. Работа с Git»</span></a></span></li></ul></nav>

    </div>
</div>
    <div  class="drawer drawer-left d-print-none not-initialized" data-region="fixed-drawer" id="theme_opentechnology-drawers-courseindex" data-preference="" data-state="show-drawer-left" data-forceopen="0" data-close-on-resize="0">
    <div class="drawerheader">
        <button
            class="btn drawertoggle icon-no-margin hidden"
            data-toggler="drawers"
            data-action="closedrawer"
            data-target="theme_opentechnology-drawers-courseindex"
            data-toggle="tooltip"
            data-placement="right"
            title="Закрыть оглавление курса"
        >
            <i class="icon fa fa-times fa-fw " aria-hidden="true"  ></i>
        </button>
    </div>
    <div class="drawercontent drag-container" data-usertour="scroller">
                    <nav id="courseindex" class="courseindex">
    <div id="courseindex-content">
        <div data-region="loading-placeholder-content" aria-hidden="true" id="course-index-placeholder">
            <ul class="media-list">
                <li class="media">
                    <div class="media-body col-md-6 p-0 d-flex align-items-center">
                        <div class="bg-pulse-grey rounded-circle mr-2"></div>
                        <div class="bg-pulse-grey w-100"></div>
                    </div>
                </li>
                <li class="media">
                    <div class="media-body col-md-6 p-0 d-flex align-items-center">
                        <div class="bg-pulse-grey rounded-circle mr-2"></div>
                        <div class="bg-pulse-grey w-100"></div>
                    </div>
                </li>
                <li class="media">
                    <div class="media-body col-md-6 p-0 d-flex align-items-center">
                        <div class="bg-pulse-grey rounded-circle mr-2"></div>
                        <div class="bg-pulse-grey w-100"></div>
                    </div>
                </li>
                <li class="media">
                    <div class="media-body col-md-6 p-0 d-flex align-items-center">
                        <div class="bg-pulse-grey rounded-circle mr-2"></div>
                        <div class="bg-pulse-grey w-100"></div>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>

    </div>
</div>
</div><div class="clearfix"></div>
<div id="blocks-content-heading-wrapper">
    <div id="blocks-content-heading-position" class="container-fluid ">
        <aside id="block-region-content-heading" class=" block-region" data-blockregion="content-heading" data-droptarget="1"></aside>    </div>
</div>

<div id="page-wrapper">
    <div class="container-fluid ">
        <div id="page" class="row-fluid">
        	<div class="page-wrapper col-md-12">
                <div id="page-content" class="row   d-print-block">
    <div id="region-main-box" class="region-main">
        <section id="region-main" class="region-main-content" aria-label="Содержимое">

                <header class="d-print-none mt-6 mb-1">
    <div class="w-100">
        <div class="d-flex flex-wrap align-items-center">
            <div id="page-navbar">
                <nav aria-label="Панель навигации">
    <ol class="breadcrumb">
                <li class="breadcrumb-item">
                    <a href="https://edu.stankin.ru/"  >В начало</a>
                </li>

                <li class="breadcrumb-item">
                    <a href="https://edu.stankin.ru/course/index.php?categoryid=446"  >Бакалавриат (ФГОС 3++)</a>
                </li>

                <li class="breadcrumb-item">
                    <a href="https://edu.stankin.ru/course/index.php?categoryid=440"  >УГСН 09.00.00 (ФГОС 3++)</a>
                </li>

                <li class="breadcrumb-item">
                    <a href="https://edu.stankin.ru/course/index.php?categoryid=445"  >Общие дисциплины (09 группа)</a>
                </li>

                <li class="breadcrumb-item">
                    <a href="https://edu.stankin.ru/local/crw/course.php?id=11060"  title="О курсе">О курсе</a>
                </li>

                <li class="breadcrumb-item">
                    <a href="https://edu.stankin.ru/course/view.php?id=11060#section-14"  title="Прикладное программирование">Прикл. прогр. (090303++)</a>
                </li>

                <li class="breadcrumb-item"><span>Лабораторная работа № 3 «Регулярные выражения. Работа с Git»</span></li>
        </ol>
</nav>
            </div>
            <div class="ml-auto d-flex">

            </div>
            <div id="course-header">

            </div>
        </div>
        <div class="d-flex align-items-center">
                    <div class="mr-auto">
                        <div class="page-context-header"><div class="page-header-headings"><h1>Прикладное программирование</h1></div></div>
                    </div>
            <div class="header-actions-container ml-auto" data-region="header-actions-container">
            </div>
        </div>
    </div>
</header>

                <aside id="block-region-side-content-top" class="block-region" data-blockregion="side-content-top" data-droptarget="1"></aside>


            	<span class="notifications" id="user-notifications"></span>

                <span id="maincontent"></span>
                    <h2>Лабораторная работа № 3 «Регулярные выражения. Работа с Git»</h2>
                <div class="activity-header" data-for="page-activity-header">                        <div class="activity-description" id="intro">
                            <div class="box py-3 generalbox boxaligncenter"><div class="no-overflow"><p dir="ltr" style="text-align: left;"></p><p dir="ltr">Технологии: регулярные выражения (C++, Python), системы контроля версий.</p><p dir="ltr">Инструменты: QT, PyCharm, git.</p><p dir="ltr">Лабораторная работа № 3. Регулярные выражения. Работа с Git.</p><p dir="ltr"><span style="font-size: 0.9375rem;">1) Выполнить задание на тему регулярного выражения (предложив свой вариант или по вариантам (не более 2 человек на 1 вариант).</span><br></p><p dir="ltr">2) Для хранения кода используйте git (например github.com или bitbucket.org). Создать не менее двух коммитов.</p><p dir="ltr">2) Подготовить отчёт о выполненной лабораторной работе. Подготовиться по вопросам к защите.</p><p dir="ltr"><br></p><p dir="ltr">Полезные ссылки: интерактивный тренажёр https://learngitbranching.js.org/, книга&nbsp;<span style="font-size: 0.9375rem;">https://git-scm.com/book/ru/v2/.&nbsp;</span></p><p dir="ltr"><br></p><p dir="ltr">Варианты (балл не выше 34):</p><p>1. Слова в алфавите {a, b}, такие, что на третьем месте от начала слова&nbsp;<span style="font-size: 0.9375rem;">стоит буква а, а на пятом месте с конца – буква b.</span></p><p>2. Слова в алфавите {a, b}, в которых число букв четно.</p><p>3. Слова в алфавите {a, b}, не содержащие подстроки ab.</p><p>4. Слова в алфавите {a, b}, не содержащие подстроки aab.</p><p>5. Слова в алфавите {a, b, c}, в которых нет двух соседних букв b.</p><p>6. Выведите все цифры введённой строки.</p><p>7. Выведите все буквы введённой строки.</p><p>8. Выведите все строчные буквы введённой строки.</p><p>9. Выведите все прописные буквы введённой строки.</p><p>10.</p><p><br></p><p>Варианты (балл не выше 44):<br></p><p>11. Слова в алфавите {a, b, c}, содержащие подслово вида bxa, где x –&nbsp;<span style="font-size: 0.9375rem;">произвольная буква алфавита.</span></p><p>12. Слова в алфавите {a, b, c}, в которых за буквой а обязательно следует&nbsp;<span style="font-size: 0.9375rem;">буква с.</span></p><p>13.&nbsp;<span style="font-size: 0.9375rem;">Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.</span></p><p><span style="font-size: 0.9375rem;">14. Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).<br></span></p><p><span style="font-size: 0.9375rem;">15. Проверить, что строка содержит синтаксически корректный IP-адрес&nbsp;</span><span style="font-size: 0.9375rem;">(IPv4).</span></p><p>16. Проверить, что строка является синтаксически корректным почтовым индексом.</p><p>17. Проверить, что строка является синтаксически корректным доменным именем.</p><p><span style=""></span></p><p>18. Проверить, что строка является синтаксически корректным цветом в формате HEX.</p><p>19.&nbsp;Проверить, что строка является синтаксически корректным номером телефона.</p><p>20.</p><p><br></p><p>Варианты (балл не выше 54):</p><p>21. Из документа HTML вывести все e-mail.</p><p>22. Из документа HTML вывести имена файлов, которые указаны в ссылках на другие документы.</p><p>23. Из документа HTML вывести все гиперссылки.</p><p>24.&nbsp;<span style="font-size: 0.9375rem;">Выведите строки, содержащие двоичную запись числа, кратного 3.</span></p><p>25. Проверить, что строка является синтаксически корректным&nbsp;<span style="font-size: 0.9375rem;">математическим выражением. Математическое выражение может&nbsp;</span><span style="font-size: 0.9375rem;">содержать ч</span><span style="font-size: 0.9375rem;">исла, о</span><span style="font-size: 0.9375rem;">дносимвольные переменные, з</span><span style="font-size: 0.9375rem;">наки математических операций, круглые&nbsp;</span><span style="font-size: 0.9375rem;">скобки</span><span style="font-size: 0.9375rem;">.</span></p><p>Корректные примеры: 17*4+(x-54/(2+4))=y, 2+2, 18-41*с.</p><p>Некорректные примеры: +45, 17+4*, (34+1, 45-3), (4+5)).</p><p>26.&nbsp;<span style="font-size: 0.9375rem;">Проверить, что строка является синтаксически корректным СНИЛС.</span></p><p><br></p><p><br></p><p>Вопросы к защите.</p><p><span style="font-size: 14.939px;">1) Понятие регулярных выражений.<br></span></p><p><span style="font-size: 14.939px;">2) Регулярные выражения в Python.</span></p><p><span style="font-size: 14.939px;">3) Регулярные выражения в С++.</span></p><p><span style="font-size: 14.939px;">4) Понятие систем контроля версий.</span></p><p>5) Понятие Git.<br></p><p>6) Основные понятия в Git.<br></p><p>7) Git: состояния файла.<br></p><p>8) Основные команды в Git.<br></p><p>9) Слияния и конфликты в Git.</p><p>10)&nbsp;Непрерывная интеграция.</p><p></p></div></div>
                        </div>
                    </div>




            <div role="main"><div class="container-fluid mb-4">
    <div class="row">
        <div class="col-xs-6 mr-3">
                    <div class="singlebutton">
                        <form method="get" action="https://edu.stankin.ru/mod/assign/view.php" >
                                <input type="hidden" name="id" value="380903">
                                <input type="hidden" name="action" value="editsubmission">
                            <button type="submit" class="btn btn-primary"
                                id="single_button656b0a6ba1c2e64"


                                >Добавить ответ на задание</button>
                        </form>
                    </div>
        </div>
    </div>
</div><div class="submissionstatustable"><h3>Состояние ответа</h3><div class="box py-3 boxaligncenter submissionsummarytable"><div class="table-responsive"><table class="generaltable table-bordered">
<tbody><tr class="">
<th class="cell c0" style="" scope="row">Состояние ответа на задание</th>
<td class="cell c1 lastcol" style="">Ответы на задание еще не представлены</td>
</tr>
<tr class="lastrow">
<th class="cell c0" style="" scope="row">Состояние оценивания</th>
<td class="submissionnotgraded cell c1 lastcol" style="">Не оценено</td>
</tr>
</tbody>
</table>
</div></div></div></div>

            	<div class="mt-4 mb-1 activity-navigation container-fluid">
<div class="row">
    <div class="col-md-4">        <div class="float-left">
                <a href="https://edu.stankin.ru/mod/assign/view.php?id=379455&forceview=1" id="prev-activity-link" class="btn btn-link" >&#9668; Лабораторная работа № 2 «Python: оконные приложения. C++: STL»</a>

        </div>
</div>
    <div class="col-md-4">        <div class="mdl-align">
            <div class="urlselect">
    <form method="post" action="https://edu.stankin.ru/course/jumpto.php" class="form-inline" id="url_select_f656b0a6ba1c2e61">
        <input type="hidden" name="sesskey" value="0ldtSfBaXr">
            <label for="jump-to-activity" class="sr-only">
                Перейти на...
            </label>
        <select  id="jump-to-activity" class="custom-select urlselect" name="jump"
                 >
                    <option value="" selected>Перейти на...</option>
                    <option value="/mod/resource/view.php?id=345501&amp;forceview=1" >Аннотация рабочей программы</option>
                    <option value="/mod/resource/view.php?id=345499&amp;forceview=1" >Рабочая программа дисциплины</option>
                    <option value="/mod/forum/view.php?id=79268&amp;forceview=1" >Объявления</option>
                    <option value="/mod/forum/view.php?id=79269&amp;forceview=1" >Вопросы и ответы</option>
                    <option value="/mod/page/view.php?id=378616&amp;forceview=1" >Рекомендуемые онлайн-курсы.</option>
                    <option value="/mod/resource/view.php?id=345478&amp;forceview=1" >Лекция. Введение</option>
                    <option value="/mod/resource/view.php?id=345479&amp;forceview=1" >Лекция. Обработка ошибок</option>
                    <option value="/mod/resource/view.php?id=345481&amp;forceview=1" >Лекция. Приложения с графическим интерфейсом</option>
                    <option value="/mod/resource/view.php?id=345482&amp;forceview=1" >Лекция. Принципы SOLID</option>
                    <option value="/mod/page/view.php?id=345562&amp;forceview=1" >Практическое занятие (семинар). Принципы SOLID</option>
                    <option value="/mod/resource/view.php?id=345483&amp;forceview=1" >Лекция. Системы контроля версий</option>
                    <option value="/mod/resource/view.php?id=345484&amp;forceview=1" >Лекция. Стандартная библиотека шаблонов (STL)</option>
                    <option value="/mod/resource/view.php?id=345485&amp;forceview=1" >Лекция. Работа с данными</option>
                    <option value="/mod/page/view.php?id=343616&amp;forceview=1" >Вопросы для подготовки к экзамену</option>
                    <option value="/mod/url/view.php?id=381117&amp;forceview=1" >Успеваемость и варианты ИДБ-22-11</option>
                    <option value="/mod/resource/view.php?id=323234&amp;forceview=1" >Шаблон отчета по ЛР</option>
                    <option value="/mod/page/view.php?id=328359&amp;forceview=1" >Структура отчетов для ЛР 1, 2, 3 и 4</option>
                    <option value="/mod/url/view.php?id=323976&amp;forceview=1" >Google Colab по ЛР №1</option>
                    <option value="/mod/url/view.php?id=324497&amp;forceview=1" >Google Colab по ЛР №2. Qt + STL</option>
                    <option value="/mod/url/view.php?id=326471&amp;forceview=1" >Google Colab по ЛР №3. Regex, Git</option>
                    <option value="/mod/assign/view.php?id=376884&amp;forceview=1" >Лабораторная работа № 1 «ООП в Python. Обработка исключительных ситуаций. Форматы XML и JSON»</option>
                    <option value="/mod/assign/view.php?id=379455&amp;forceview=1" >Лабораторная работа № 2 «Python: оконные приложения. C++: STL»</option>
                    <option value="/mod/assign/view.php?id=380904&amp;forceview=1" >Лабораторная работа № 4 «Анализ данных. Работа с API, создание чат-бота»</option>
                    <option value="/mod/resource/view.php?id=384127&amp;forceview=1" >Семинар 1</option>
                    <option value="/mod/resource/view.php?id=384129&amp;forceview=1" >Семинар 2</option>
        </select>
            <noscript>
                <input type="submit" class="btn btn-secondary ml-1" value="Применить">
            </noscript>
    </form>
</div>

        </div>
</div>
    <div class="col-md-4">        <div class="float-right">
                <a href="https://edu.stankin.ru/mod/assign/view.php?id=380904&forceview=1" id="next-activity-link" class="btn btn-link" >Лабораторная работа № 4 «Анализ данных. Работа с API, создание чат-бота» &#9658;</a>

        </div>
</div>
</div>
</div>


            	<aside id="block-region-side-content-bot" class="block-region" data-blockregion="side-content-bot" data-droptarget="1"></aside>
        </section>
    </div>

    <div class="columnleft blockcolumn  mt-6">
        <section data-region="blocks-column" class="d-print-none" aria-label="Блоки">
            <aside id="block-region-side-pre" class="block-region" data-blockregion="side-pre" data-droptarget="1"></aside>
        </section>
    </div>

</div>            </div>
        </div>
        <div
    id="drawer-656b0a6ba8eb3656b0a6ba1c2e62"
    class=" drawer bg-white hidden"
    aria-expanded="false"
    aria-hidden="true"
    data-region="right-hand-drawer"
    role="region"
    tabindex="0"
>
            <div id="message-drawer-656b0a6ba8eb3656b0a6ba1c2e62" class="message-app" data-region="message-drawer" role="region">
            <div class="closewidget text-right pr-2">
                <a class="text-dark btn-link" data-action="closedrawer" href="#"
                   title="Закрыть" aria-label="Закрыть"
                >
                    <img class="icon oticon" alt="" aria-hidden="true" src="https://edu.stankin.ru/theme/image.php/opentechnology/core/1701486024/t/dockclose" />
                </a>
            </div>
            <div class="header-container position-relative" data-region="header-container">
                <div class="hidden border-bottom p-1 px-sm-2" aria-hidden="true" data-region="view-contacts">
                    <div class="d-flex align-items-center">
                        <div class="align-self-stretch">
                            <a class="h-100 d-flex align-items-center mr-2" href="#" data-route-back role="button">
                                <div class="icon-back-in-drawer">
                                    <span class="dir-rtl-hide"><i class="icon fa fa-chevron-left fa-fw " aria-hidden="true"  ></i></span>
                                    <span class="dir-ltr-hide"><i class="icon fa fa-chevron-right fa-fw " aria-hidden="true"  ></i></span>
                                </div>
                                <div class="icon-back-in-app">
                                    <span class="dir-rtl-hide"><i class="icon fa fa-times fa-fw " aria-hidden="true"  ></i></span>
                                </div>                            </a>
                        </div>
                        <div>
                            Собеседники
                        </div>
                        <div class="ml-auto">
                            <a href="#" data-route="view-search" role="button" aria-label="Поиск">
                                <img class="icon oticon" alt="" aria-hidden="true" src="https://edu.stankin.ru/theme/image.php/opentechnology/core/1701486024/a/search" />
                            </a>
                        </div>
                    </div>
                </div>                
                <div
                    class="hidden bg-white position-relative border-bottom p-1 px-sm-2"
                    aria-hidden="true"
                    data-region="view-conversation"
                >
                    <div class="hidden" data-region="header-content"></div>
                    <div class="hidden" data-region="header-edit-mode">

                        <div class="d-flex p-2 align-items-center">
                            Выбранные сообщения:
                            <span class="ml-1" data-region="message-selected-court">1</span>
                            <button type="button" class="ml-auto close" aria-label="Отменить выбор сообщения"
                                data-action="cancel-edit-mode">
                                    <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                    </div>
                    <div data-region="header-placeholder">
                        <div class="d-flex">
                            <div
                                class="ml-2 rounded-circle bg-pulse-grey align-self-center"
                                style="height: 38px; width: 38px"
                            >
                            </div>
                            <div class="ml-2 " style="flex: 1">
                                <div
                                    class="mt-1 bg-pulse-grey w-75"
                                    style="height: 16px;"
                                >
                                </div>
                            </div>
                            <div
                                class="ml-2 bg-pulse-grey align-self-center"
                                style="height: 16px; width: 20px"
                            >
                            </div>
                        </div>
                    </div>
                    <div
                        class="hidden position-absolute z-index-1"
                        data-region="confirm-dialogue-container"
                        style="top: 0; bottom: -1px; right: 0; left: 0; background: rgba(0,0,0,0.3);"
                    ></div>
                </div>                <div class="border-bottom p-1 px-sm-2" aria-hidden="false"  data-region="view-overview">
                    <div class="d-flex align-items-center">
                        <div class="input-group simplesearchform">
                            <input
                                type="text"
                                class="form-control"
                                placeholder="Поиск"
                                aria-label="Поиск"
                                data-region="view-overview-search-input"
                            >
                            <div class="input-group-append">
                                <span class="icon-no-margin btn btn-submit">
                                    <img class="icon oticon" alt="" aria-hidden="true" src="https://edu.stankin.ru/theme/image.php/opentechnology/core/1701486024/a/search" />
                                </span>
                            </div>
                        </div>
                        <div class="ml-2">
                            <a
                                href="#"
                                data-route="view-settings"
                                data-route-param="24186"
                                aria-label="Настройки"
                                role="button"
                            >
                                <i class="icon fa fa-cog fa-fw " aria-hidden="true"  ></i>
                            </a>
                        </div>
                    </div>
                    <div class="text-right mt-sm-3">
                        <a href="#" data-route="view-contacts" role="button">
                            <i class="icon fa fa-user fa-fw " aria-hidden="true"  ></i>
                            Собеседники
                            <span
                                class="badge badge-primary bg-primary ml-2 hidden"
                                data-region="contact-request-count"
                            >
                                <span aria-hidden="true">0</span>
                                <span class="sr-only">Ожидающих запросов на добавление в собеседники: 0</span>
                            </span>
                        </a>
                    </div>
                </div>

                <div class="hidden border-bottom p-1 px-sm-2 view-search"  aria-hidden="true" data-region="view-search">
                    <div class="d-flex align-items-center">
                        <a
                            class="mr-2 align-self-stretch d-flex align-items-center"
                            href="#"
                            data-route-back
                            data-action="cancel-search"
                            role="button"
                        >
                            <div class="icon-back-in-drawer">
                                <span class="dir-rtl-hide"><i class="icon fa fa-chevron-left fa-fw " aria-hidden="true"  ></i></span>
                                <span class="dir-ltr-hide"><i class="icon fa fa-chevron-right fa-fw " aria-hidden="true"  ></i></span>
                            </div>
                            <div class="icon-back-in-app">
                                <span class="dir-rtl-hide"><i class="icon fa fa-times fa-fw " aria-hidden="true"  ></i></span>
                            </div>                        </a>
                        <div class="input-group simplesearchform">
                            <input
                                type="text"
                                class="form-control"
                                placeholder="Поиск"
                                aria-label="Поиск"
                                data-region="search-input"
                            >
                            <div class="input-group-append">
                                <button
                                    class="btn btn-submit icon-no-margin"
                                    type="button"
                                    data-action="search"
                                    aria-label="Поиск"
                                >
                                    <span data-region="search-icon-container">
                                        <img class="icon oticon" alt="" aria-hidden="true" src="https://edu.stankin.ru/theme/image.php/opentechnology/core/1701486024/a/search" />
                                    </span>
                                    <span class="hidden" data-region="loading-icon-container">
                                        <span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
                                    </span>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>                
                <div class="hidden border-bottom p-1 px-sm-2 pb-sm-3" aria-hidden="true" data-region="view-settings">
                    <div class="d-flex align-items-center">
                        <div class="align-self-stretch" >
                            <a class="h-100 d-flex mr-2 align-items-center" href="#" data-route-back role="button">
                                <div class="icon-back-in-drawer">
                                    <span class="dir-rtl-hide"><i class="icon fa fa-chevron-left fa-fw " aria-hidden="true"  ></i></span>
                                    <span class="dir-ltr-hide"><i class="icon fa fa-chevron-right fa-fw " aria-hidden="true"  ></i></span>
                                </div>
                                <div class="icon-back-in-app">
                                    <span class="dir-rtl-hide"><i class="icon fa fa-times fa-fw " aria-hidden="true"  ></i></span>
                                </div>                            </a>
                        </div>
                        <div>
                            Настройки
                        </div>
                    </div>
                </div>
            </div>
            <div class="body-container position-relative" data-region="body-container">

                <div
                    class="hidden"
                    data-region="view-contact"
                    aria-hidden="true"
                >
                    <div class="p-2 pt-3" data-region="content-container"></div>
                </div>                <div class="hidden h-100" data-region="view-contacts" aria-hidden="true" data-user-id="24186">
                    <div class="d-flex flex-column h-100">
                        <div class="p-3 border-bottom">
                            <ul class="nav nav-pills nav-fill" role="tablist">
                                <li class="nav-item">
                                    <a
                                        id="contacts-tab-656b0a6ba8eb3656b0a6ba1c2e62"
                                        class="nav-link active"
                                        href="#contacts-tab-panel-656b0a6ba8eb3656b0a6ba1c2e62"
                                        data-toggle="tab"
                                        data-action="show-contacts-section"
                                        role="tab"
                                        aria-controls="contacts-tab-panel-656b0a6ba8eb3656b0a6ba1c2e62"
                                        aria-selected="true"
                                    >
                                        Собеседники
                                    </a>
                                </li>
                                <li class="nav-item">
                                    <a
                                        id="requests-tab-656b0a6ba8eb3656b0a6ba1c2e62"
                                        class="nav-link"
                                        href="#requests-tab-panel-656b0a6ba8eb3656b0a6ba1c2e62"
                                        data-toggle="tab"
                                        data-action="show-requests-section"
                                        role="tab"
                                        aria-controls="requests-tab-panel-656b0a6ba8eb3656b0a6ba1c2e62"
                                        aria-selected="false"
                                    >
                                        Запросы
                                        <span class="badge badge-primary bg-primary ml-2 hidden"
                                            data-region="contact-request-count"
                                        >
                                            <span aria-hidden="true">0</span>
                                            <span class="sr-only">Ожидающих запросов на добавление в собеседники: 0</span>
                                        </span>
                                    </a>
                                </li>
                            </ul>
                        </div>
                        <div class="tab-content d-flex flex-column h-100">
                                            <div
                    class="tab-pane fade show active h-100 lazy-load-list"
                    aria-live="polite"
                    data-region="lazy-load-list"
                    data-user-id="24186"
                                        id="contacts-tab-panel-656b0a6ba8eb3656b0a6ba1c2e62"
                    data-section="contacts"
                    role="tabpanel"
                    aria-labelledby="contacts-tab-656b0a6ba8eb3656b0a6ba1c2e62"

                >

                    <div class="hidden text-center p-2" data-region="empty-message-container">
                        Нет контактов
                    </div>
                    <div class="hidden list-group" data-region="content-container">

                    </div>
                    <div class="list-group" data-region="placeholder-container">

                    </div>
                    <div class="w-100 text-center p-3 hidden" data-region="loading-icon-container" >
                        <span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
                    </div>
                </div>

                                            <div
                    class="tab-pane fade h-100 lazy-load-list"
                    aria-live="polite"
                    data-region="lazy-load-list"
                    data-user-id="24186"
                                        id="requests-tab-panel-656b0a6ba8eb3656b0a6ba1c2e62"
                    data-section="requests"
                    role="tabpanel"
                    aria-labelledby="requests-tab-656b0a6ba8eb3656b0a6ba1c2e62"

                >

                    <div class="hidden text-center p-2" data-region="empty-message-container">
                        Нет запросов на добавление в контакты
                    </div>
                    <div class="hidden list-group" data-region="content-container">

                    </div>
                    <div class="list-group" data-region="placeholder-container">

                    </div>
                    <div class="w-100 text-center p-3 hidden" data-region="loading-icon-container" >
                        <span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
                    </div>
                </div>
                        </div>
                    </div>
                </div>

                <div
                    class="view-conversation hidden h-100"
                    aria-hidden="true"
                    data-region="view-conversation"
                    data-user-id="24186"
                    data-midnight="1701464400"
                    data-message-poll-min="10"
                    data-message-poll-max="120"
                    data-message-poll-after-max="300"
                    style="overflow-y: auto; overflow-x: hidden"
                >
                    <div class="position-relative h-100" data-region="content-container" style="overflow-y: auto; overflow-x: hidden">
                        <div class="content-message-container hidden h-100 px-2 pt-0" data-region="content-message-container" role="log" style="overflow-y: auto; overflow-x: hidden">
                            <div class="py-3 sticky-top z-index-1 border-bottom text-center hidden" data-region="contact-request-sent-message-container">
                                <p class="m-0">Запрос на добавление в контакты отправлен</p>
                                <p class="font-italic font-weight-light" data-region="text"></p>
                            </div>
                            <div class="p-3 text-center hidden" data-region="self-conversation-message-container">
                                <p class="m-0">Личное пространство</p>
                                <p class="font-italic font-weight-light" data-region="text">Сохраните черновики сообщений, ссылок, заметок и т.п. К ним можно будет вернуться позже.</p>
                           </div>
                            <div class="hidden text-center p-3" data-region="more-messages-loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
</div>
                        </div>
                        <div class="p-4 w-100 h-100 hidden position-absolute z-index-1" data-region="confirm-dialogue-container" style="top: 0; background: rgba(0,0,0,0.3);">

                            <div class="p-3 bg-white" data-region="confirm-dialogue" role="alert">
                                <p class="text-muted" data-region="dialogue-text"></p>
                                <div class="mb-2 custom-control custom-checkbox hidden" data-region="delete-messages-for-all-users-toggle-container">
                                    <input type="checkbox" class="custom-control-input" id="delete-messages-for-all-users" data-region="delete-messages-for-all-users-toggle">
                                    <label class="custom-control-label text-muted" for="delete-messages-for-all-users">
                                        Удалить у меня и у всех остальных
                                    </label>
                                </div>
                                <button type="button" class="btn btn-primary btn-block hidden" data-action="confirm-block">
                                    <span data-region="dialogue-button-text">Блок</span>
                                    <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
</span>
                                </button>
                                <button type="button" class="btn btn-primary btn-block hidden" data-action="confirm-unblock">
                                    <span data-region="dialogue-button-text">Разблокировать</span>
                                    <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
</span>
                                </button>
                                <button type="button" class="btn btn-primary btn-block hidden" data-action="confirm-remove-contact">
                                    <span data-region="dialogue-button-text">Удалить</span>
                                    <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
</span>
                                </button>
                                <button type="button" class="btn btn-primary btn-block hidden" data-action="confirm-add-contact">
                                    <span data-region="dialogue-button-text">Добавить</span>
                                    <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
</span>
                                </button>
                                <button type="button" class="btn btn-primary btn-block hidden" data-action="confirm-delete-selected-messages">
                                    <span data-region="dialogue-button-text">Удалить</span>
                                    <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
</span>
                                </button>
                                <button type="button" class="btn btn-primary btn-block hidden" data-action="confirm-delete-conversation">
                                    <span data-region="dialogue-button-text">Удалить</span>
                                    <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
</span>
                                </button>
                                <button type="button" class="btn btn-primary btn-block hidden" data-action="request-add-contact">
                                    <span data-region="dialogue-button-text">Отправить запрос на добавление в контакты</span>
                                    <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
</span>
                                </button>
                                <button type="button" class="btn btn-primary btn-block hidden" data-action="accept-contact-request">
                                    <span data-region="dialogue-button-text">Принять и добавить в контакты</span>
                                    <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
</span>
                                </button>
                                <button type="button" class="btn btn-secondary btn-block hidden" data-action="decline-contact-request">
                                    <span data-region="dialogue-button-text">Отказаться</span>
                                    <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
</span>
                                </button>
                                <button type="button" class="btn btn-primary btn-block" data-action="okay-confirm">OK</button>
                                <button type="button" class="btn btn-secondary btn-block" data-action="cancel-confirm">Отмена</button>
                            </div>
                        </div>
                        <div class="px-2 pb-2 pt-0" data-region="content-placeholder">
                            <div class="h-100 d-flex flex-column">
                                <div
                                    class="px-2 pb-2 pt-0 bg-light h-100"
                                    style="overflow-y: auto"
                                >
                                    <div class="mt-4">
                                        <div class="mb-4">
                                            <div class="mx-auto bg-white" style="height: 25px; width: 100px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                    </div>                                    <div class="mt-4">
                                        <div class="mb-4">
                                            <div class="mx-auto bg-white" style="height: 25px; width: 100px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                    </div>                                    <div class="mt-4">
                                        <div class="mb-4">
                                            <div class="mx-auto bg-white" style="height: 25px; width: 100px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                    </div>                                    <div class="mt-4">
                                        <div class="mb-4">
                                            <div class="mx-auto bg-white" style="height: 25px; width: 100px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                    </div>                                    <div class="mt-4">
                                        <div class="mb-4">
                                            <div class="mx-auto bg-white" style="height: 25px; width: 100px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                    </div>                                </div>
                            </div>                        </div>
                    </div>
                </div>

                <div
                    class="hidden"
                    aria-hidden="true"
                    data-region="view-group-info"
                >
                    <div
                        class="pt-3 h-100 d-flex flex-column"
                        data-region="group-info-content-container"
                        style="overflow-y: auto"
                    ></div>
                </div>                <div class="h-100 view-overview-body" aria-hidden="false" data-region="view-overview"  data-user-id="24186">
                    <div id="message-drawer-view-overview-container-656b0a6ba8eb3656b0a6ba1c2e62" class="d-flex flex-column h-100" style="overflow-y: auto">


                            <div
                                class="section border-0 card rounded-0"
                                data-region="view-overview-favourites"
                            >
                                <div id="view-overview-favourites-toggle" class="card-header rounded-0" data-region="toggle">
                                    <button
                                        class="btn btn-link w-100 text-left p-1 p-sm-2 d-flex rounded-0 align-items-center overview-section-toggle collapsed"
                                        data-toggle="collapse"
                                        data-target="#view-overview-favourites-target-656b0a6ba8eb3656b0a6ba1c2e62"
                                        aria-expanded="false"
                                        aria-controls="view-overview-favourites-target-656b0a6ba8eb3656b0a6ba1c2e62"
                                    >
                                        <span class="collapsed-icon-container">
                                            <i class="icon fa fa-caret-right fa-fw " aria-hidden="true"  ></i>
                                        </span>
                                        <span class="expanded-icon-container">
                                            <i class="icon fa fa-caret-down fa-fw " aria-hidden="true"  ></i>
                                        </span>
                                        <span class="font-weight-bold">Помеченные</span>
                                        <small class="hidden ml-1" data-region="section-total-count-container">
                                            (<span aria-hidden="true" data-region="section-total-count"></span><span class="sr-only">Всего бесед: </span>)
                                        </small>
                                        <span class="hidden ml-2" data-region="loading-icon-container">
                                            <span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
                                        </span>
                                        <span
                                            class="hidden badge badge-pill badge-primary ml-auto bg-primary"
                                            data-region="section-unread-count"
                                        >
                                            <span aria-hidden="true"></span>
                                            <span class="sr-only">Непрочитанных бесед: </span>
                                        </span>
                                    </button>
                                </div>
                                                            <div
                                class="collapse border-bottom  lazy-load-list"
                                aria-live="polite"
                                data-region="lazy-load-list"
                                data-user-id="24186"
                                            id="view-overview-favourites-target-656b0a6ba8eb3656b0a6ba1c2e62"
            aria-labelledby="view-overview-favourites-toggle"
            data-parent="#message-drawer-view-overview-container-656b0a6ba8eb3656b0a6ba1c2e62"

                            >

                                <div class="hidden text-center p-2" data-region="empty-message-container">
                                            <p class="text-muted mt-2">Нет помеченных бесед</p>

                                </div>
                                <div class="hidden list-group" data-region="content-container">

                                </div>
                                <div class="list-group" data-region="placeholder-container">
                                            <div class="text-center py-2"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
</div>

                                </div>
                                <div class="w-100 text-center p-3 hidden" data-region="loading-icon-container" >
                                    <span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
                                </div>
                            </div>
                            </div>


                            <div
                                class="section border-0 card rounded-0"
                                data-region="view-overview-group-messages"
                            >
                                <div id="view-overview-group-messages-toggle" class="card-header rounded-0" data-region="toggle">
                                    <button
                                        class="btn btn-link w-100 text-left p-1 p-sm-2 d-flex rounded-0 align-items-center overview-section-toggle collapsed"
                                        data-toggle="collapse"
                                        data-target="#view-overview-group-messages-target-656b0a6ba8eb3656b0a6ba1c2e62"
                                        aria-expanded="false"
                                        aria-controls="view-overview-group-messages-target-656b0a6ba8eb3656b0a6ba1c2e62"
                                    >
                                        <span class="collapsed-icon-container">
                                            <i class="icon fa fa-caret-right fa-fw " aria-hidden="true"  ></i>
                                        </span>
                                        <span class="expanded-icon-container">
                                            <i class="icon fa fa-caret-down fa-fw " aria-hidden="true"  ></i>
                                        </span>
                                        <span class="font-weight-bold">Группа</span>
                                        <small class="hidden ml-1" data-region="section-total-count-container">
                                            (<span aria-hidden="true" data-region="section-total-count"></span><span class="sr-only">Всего бесед: </span>)
                                        </small>
                                        <span class="hidden ml-2" data-region="loading-icon-container">
                                            <span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
                                        </span>
                                        <span
                                            class="hidden badge badge-pill badge-primary ml-auto bg-primary"
                                            data-region="section-unread-count"
                                        >
                                            <span aria-hidden="true"></span>
                                            <span class="sr-only">Непрочитанных бесед: </span>
                                        </span>
                                    </button>
                                </div>
                                                            <div
                                class="collapse border-bottom  lazy-load-list"
                                aria-live="polite"
                                data-region="lazy-load-list"
                                data-user-id="24186"
                                            id="view-overview-group-messages-target-656b0a6ba8eb3656b0a6ba1c2e62"
            aria-labelledby="view-overview-group-messages-toggle"
            data-parent="#message-drawer-view-overview-container-656b0a6ba8eb3656b0a6ba1c2e62"

                            >

                                <div class="hidden text-center p-2" data-region="empty-message-container">
                                            <p class="text-muted mt-2">Нет групповых бесед</p>

                                </div>
                                <div class="hidden list-group" data-region="content-container">

                                </div>
                                <div class="list-group" data-region="placeholder-container">
                                            <div class="text-center py-2"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
</div>

                                </div>
                                <div class="w-100 text-center p-3 hidden" data-region="loading-icon-container" >
                                    <span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
                                </div>
                            </div>
                            </div>


                            <div
                                class="section border-0 card rounded-0"
                                data-region="view-overview-messages"
                            >
                                <div id="view-overview-messages-toggle" class="card-header rounded-0" data-region="toggle">
                                    <button
                                        class="btn btn-link w-100 text-left p-1 p-sm-2 d-flex rounded-0 align-items-center overview-section-toggle collapsed"
                                        data-toggle="collapse"
                                        data-target="#view-overview-messages-target-656b0a6ba8eb3656b0a6ba1c2e62"
                                        aria-expanded="false"
                                        aria-controls="view-overview-messages-target-656b0a6ba8eb3656b0a6ba1c2e62"
                                    >
                                        <span class="collapsed-icon-container">
                                            <i class="icon fa fa-caret-right fa-fw " aria-hidden="true"  ></i>
                                        </span>
                                        <span class="expanded-icon-container">
                                            <i class="icon fa fa-caret-down fa-fw " aria-hidden="true"  ></i>
                                        </span>
                                        <span class="font-weight-bold">Личное</span>
                                        <small class="hidden ml-1" data-region="section-total-count-container">
                                            (<span aria-hidden="true" data-region="section-total-count"></span><span class="sr-only">Всего бесед: </span>)
                                        </small>
                                        <span class="hidden ml-2" data-region="loading-icon-container">
                                            <span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
                                        </span>
                                        <span
                                            class="hidden badge badge-pill badge-primary ml-auto bg-primary"
                                            data-region="section-unread-count"
                                        >
                                            <span aria-hidden="true"></span>
                                            <span class="sr-only">Непрочитанных бесед: </span>
                                        </span>
                                    </button>
                                </div>
                                                            <div
                                class="collapse border-bottom  lazy-load-list"
                                aria-live="polite"
                                data-region="lazy-load-list"
                                data-user-id="24186"
                                            id="view-overview-messages-target-656b0a6ba8eb3656b0a6ba1c2e62"
            aria-labelledby="view-overview-messages-toggle"
            data-parent="#message-drawer-view-overview-container-656b0a6ba8eb3656b0a6ba1c2e62"

                            >

                                <div class="hidden text-center p-2" data-region="empty-message-container">
                                            <p class="text-muted mt-2">Нет личных бесед</p>

                                </div>
                                <div class="hidden list-group" data-region="content-container">

                                </div>
                                <div class="list-group" data-region="placeholder-container">
                                            <div class="text-center py-2"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
</div>

                                </div>
                                <div class="w-100 text-center p-3 hidden" data-region="loading-icon-container" >
                                    <span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
                                </div>
                            </div>
                            </div>
                    </div>
                </div>

                <div
                    data-region="view-search"
                    aria-hidden="true"
                    class="h-100 hidden"
                    data-user-id="24186"
                    data-users-offset="0"
                    data-messages-offset="0"
                    style="overflow-y: auto"

                >
                    <div class="hidden" data-region="search-results-container" style="overflow-y: auto">

                        <div class="d-flex flex-column">
                            <div class="mb-3 bg-white" data-region="all-contacts-container">
                                <div data-region="contacts-container"  class="pt-2">
                                    <h4 class="h6 px-2">Собеседники</h4>
                                    <div class="list-group" data-region="list"></div>
                                </div>
                                <div data-region="non-contacts-container" class="pt-2 border-top">
                                    <h4 class="h6 px-2">Собеседники отсутствуют</h4>
                                    <div class="list-group" data-region="list"></div>
                                </div>
                                <div class="text-right">
                                    <button class="btn btn-link text-primary" data-action="load-more-users">
                                        <span data-region="button-text">Загрузить больше</span>
                                        <span data-region="loading-icon-container" class="hidden"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
</span>
                                    </button>
                                </div>
                            </div>
                            <div class="bg-white" data-region="messages-container">
                                <h4 class="h6 px-2 pt-2">Сообщения</h4>
                                <div class="list-group" data-region="list"></div>
                                <div class="text-right">
                                    <button class="btn btn-link text-primary" data-action="load-more-messages">
                                        <span data-region="button-text">Загрузить больше</span>
                                        <span data-region="loading-icon-container" class="hidden"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
</span>
                                    </button>
                                </div>
                            </div>
                            <p class="hidden p-3 text-center" data-region="no-results-container">Нет результатов</p>
                        </div>                    </div>
                    <div class="hidden" data-region="loading-placeholder">
                        <div class="text-center pt-3 icon-size-4"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
</div>
                    </div>
                    <div class="p-3 text-center" data-region="empty-message-container">
                        <p>Поиск пользователей и сообщений</p>
                    </div>
                </div>                
                <div class="h-100 hidden bg-white" aria-hidden="true" data-region="view-settings">
                    <div class="hidden" data-region="content-container">

                        <div data-region="settings" class="p-3">
                            <h3 class="h6 font-weight-bold">Приватность</h3>
                            <p>Вы можете ограничить круг лиц, которые могут отправлять вам сообщения</p>
                            <div data-preference="blocknoncontacts" class="mb-3">
                                <fieldset>
                                    <legend class="sr-only">Принимать сообщения от:</legend>
                                        <div class="custom-control custom-radio mb-2">
                                            <input
                                                type="radio"
                                                name="message_blocknoncontacts"
                                                class="custom-control-input"
                                                id="block-noncontacts-656b0a6ba8eb3656b0a6ba1c2e62-1"
                                                value="1"
                                            >
                                            <label class="custom-control-label ml-2" for="block-noncontacts-656b0a6ba8eb3656b0a6ba1c2e62-1">
                                                Только мои контакты
                                            </label>
                                        </div>
                                        <div class="custom-control custom-radio mb-2">
                                            <input
                                                type="radio"
                                                name="message_blocknoncontacts"
                                                class="custom-control-input"
                                                id="block-noncontacts-656b0a6ba8eb3656b0a6ba1c2e62-0"
                                                value="0"
                                            >
                                            <label class="custom-control-label ml-2" for="block-noncontacts-656b0a6ba8eb3656b0a6ba1c2e62-0">
                                                Мои контакты и любой в моих курсах
                                            </label>
                                        </div>
                                </fieldset>
                            </div>

                            <div class="hidden" data-region="notification-preference-container">
                                <h3 class="mb-2 mt-4 h6 font-weight-bold">Настройка уведомлений</h3>
                            </div>

                            <h3 class="mb-2 mt-4 h6 font-weight-bold">Основные</h3>
                            <div data-preference="entertosend">
                                <div class="custom-control custom-switch">
                                    <input type="checkbox" class="custom-control-input" id="enter-to-send-656b0a6ba8eb3656b0a6ba1c2e62" >
                                    <label class="custom-control-label" for="enter-to-send-656b0a6ba8eb3656b0a6ba1c2e62">
                                        Использовать Enter для отправки
                                    </label>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div data-region="placeholder-container">

                        <div class="d-flex flex-column p-3">
                            <div class="w-25 bg-pulse-grey h6" style="height: 18px"></div>
                            <div class="w-75 bg-pulse-grey mb-4" style="height: 18px"></div>
                            <div class="mb-3">
                                <div class="w-100 d-flex mb-3">
                                    <div class="bg-pulse-grey rounded-circle" style="width: 18px; height: 18px"></div>
                                    <div class="bg-pulse-grey w-50 ml-2" style="height: 18px"></div>
                                </div>
                                <div class="w-100 d-flex mb-3">
                                    <div class="bg-pulse-grey rounded-circle" style="width: 18px; height: 18px"></div>
                                    <div class="bg-pulse-grey w-50 ml-2" style="height: 18px"></div>
                                </div>
                                <div class="w-100 d-flex mb-3">
                                    <div class="bg-pulse-grey rounded-circle" style="width: 18px; height: 18px"></div>
                                    <div class="bg-pulse-grey w-50 ml-2" style="height: 18px"></div>
                                </div>
                            </div>
                            <div class="w-50 bg-pulse-grey h6 mb-3 mt-2" style="height: 18px"></div>
                            <div class="mb-4">
                                <div class="w-100 d-flex mb-2 align-items-center">
                                    <div class="bg-pulse-grey w-25" style="width: 18px; height: 27px"></div>
                                    <div class="bg-pulse-grey w-25 ml-2" style="height: 18px"></div>
                                </div>
                                <div class="w-100 d-flex mb-2 align-items-center">
                                    <div class="bg-pulse-grey w-25" style="width: 18px; height: 27px"></div>
                                    <div class="bg-pulse-grey w-25 ml-2" style="height: 18px"></div>
                                </div>
                            </div>
                            <div class="w-25 bg-pulse-grey h6 mb-3 mt-2" style="height: 18px"></div>
                            <div class="mb-3">
                                <div class="w-100 d-flex mb-2 align-items-center">
                                    <div class="bg-pulse-grey w-25" style="width: 18px; height: 27px"></div>
                                    <div class="bg-pulse-grey w-50 ml-2" style="height: 18px"></div>
                                </div>
                            </div>
                        </div>                    </div>
                </div>            </div>
            <div class="footer-container position-relative" data-region="footer-container">

                <div
                    class="hidden border-top bg-white position-relative"
                    aria-hidden="true"
                    data-region="view-conversation"
                    data-enter-to-send="0"
                >
                    <div class="hidden p-sm-2" data-region="content-messages-footer-container">

                            <div
                                class="emoji-auto-complete-container w-100 hidden"
                                data-region="emoji-auto-complete-container"
                                aria-live="polite"
                                aria-hidden="true"
                            >
                            </div>
                        <div class="d-flex mt-sm-1">
                            <textarea
                                dir="auto"
                                data-region="send-message-txt"
                                class="form-control bg-light"
                                rows="3"
                                data-auto-rows
                                data-min-rows="3"
                                data-max-rows="5"
                                aria-label="Напишите сообщение..."
                                placeholder="Напишите сообщение..."
                                style="resize: none"
                                maxlength="4096"
                            ></textarea>

                            <div class="position-relative d-flex flex-column">
                                    <div
                                        data-region="emoji-picker-container"
                                        class="emoji-picker-container hidden"
                                        aria-hidden="true"
                                    >

                                        <div
                                            data-region="emoji-picker"
                                            class="card shadow emoji-picker"
                                        >
                                            <div class="card-header px-1 pt-1 pb-0 d-flex justify-content-between flex-shrink-0">
                                                <button
                                                    class="btn btn-outline-secondary icon-no-margin category-button rounded-0 selected"
                                                    data-action="show-category"
                                                    data-category="Recent"
                                                    title="Последний"
                                                >
                                                    <i class="icon fa fa-clock-o fa-fw " aria-hidden="true"  ></i>
                                                </button>
                                                <button
                                                    class="btn btn-outline-secondary icon-no-margin category-button rounded-0"
                                                    data-action="show-category"
                                                    data-category="Smileys & Emotion"
                                                    title="Смайлики и эмоции"
                                                >
                                                    <i class="icon fa fa-smile-o fa-fw " aria-hidden="true"  ></i>
                                                </button>
                                                <button
                                                    class="btn btn-outline-secondary icon-no-margin category-button rounded-0"
                                                    data-action="show-category"
                                                    data-category="People & Body"
                                                    title="Люди и тело"
                                                >
                                                    <i class="icon fa fa-male fa-fw " aria-hidden="true"  ></i>
                                                </button>
                                                <button
                                                    class="btn btn-outline-secondary icon-no-margin category-button rounded-0"
                                                    data-action="show-category"
                                                    data-category="Animals & Nature"
                                                    title="Животные и природа"
                                                >
                                                    <i class="icon fa fa-leaf fa-fw " aria-hidden="true"  ></i>
                                                </button>
                                                <button
                                                    class="btn btn-outline-secondary icon-no-margin category-button rounded-0"
                                                    data-action="show-category"
                                                    data-category="Food & Drink"
                                                    title="Еда и питьё"
                                                >
                                                    <i class="icon fa fa-cutlery fa-fw " aria-hidden="true"  ></i>
                                                </button>
                                                <button
                                                    class="btn btn-outline-secondary icon-no-margin category-button rounded-0"
                                                    data-action="show-category"
                                                    data-category="Travel & Places"
                                                    title="Путешествия и места"
                                                >
                                                    <i class="icon fa fa-plane fa-fw " aria-hidden="true"  ></i>
                                                </button>
                                                <button
                                                    class="btn btn-outline-secondary icon-no-margin category-button rounded-0"
                                                    data-action="show-category"
                                                    data-category="Activities"
                                                    title="Мероприятия"
                                                >
                                                    <i class="icon fa fa-futbol-o fa-fw " aria-hidden="true"  ></i>
                                                </button>
                                                <button
                                                    class="btn btn-outline-secondary icon-no-margin category-button rounded-0"
                                                    data-action="show-category"
                                                    data-category="Objects"
                                                    title="Предметы"
                                                >
                                                    <i class="icon fa fa-lightbulb-o fa-fw " aria-hidden="true"  ></i>
                                                </button>
                                                <button
                                                    class="btn btn-outline-secondary icon-no-margin category-button rounded-0"
                                                    data-action="show-category"
                                                    data-category="Symbols"
                                                    title="Символы"
                                                >
                                                    <i class="icon fa fa-heart fa-fw " aria-hidden="true"  ></i>
                                                </button>
                                                <button
                                                    class="btn btn-outline-secondary icon-no-margin category-button rounded-0"
                                                    data-action="show-category"
                                                    data-category="Flags"
                                                    title="Флаги"
                                                >
                                                    <i class="icon fa fa-flag fa-fw " aria-hidden="true"  ></i>
                                                </button>
                                            </div>
                                            <div class="card-body p-2 d-flex flex-column overflow-hidden">
                                                <div class="input-group mb-1 flex-shrink-0">
                                                    <div class="input-group-prepend">
                                                        <span class="input-group-text pr-0 bg-white text-muted">
                                                            <i class="icon fa fa-search fa-fw " aria-hidden="true"  ></i>
                                                        </span>
                                                    </div>
                                                    <input
                                                        type="text"
                                                        class="form-control border-left-0"
                                                        placeholder="Найти"
                                                        aria-label="Найти"
                                                        data-region="search-input"
                                                    >
                                                </div>
                                                <div class="flex-grow-1 overflow-auto emojis-container h-100" data-region="emojis-container">
                                                    <div class="position-relative" data-region="row-container"></div>
                                                </div>
                                                <div class="flex-grow-1 overflow-auto search-results-container h-100 hidden" data-region="search-results-container">
                                                    <div class="position-relative" data-region="row-container"></div>
                                                </div>
                                            </div>
                                            <div
                                                class="card-footer d-flex flex-shrink-0"
                                                data-region="footer"
                                            >
                                                <div class="emoji-preview" data-region="emoji-preview"></div>
                                                <div data-region="emoji-short-name" class="emoji-short-name text-muted text-wrap ml-2"></div>
                                            </div>
                                        </div>
                                    </div>
                                    <button
                                        class="btn btn-link btn-icon icon-size-3 ml-1"
                                        aria-label="Переключить выбор эмодзи"
                                        data-action="toggle-emoji-picker"
                                    >
                                        <i class="icon fa fa-smile-o fa-fw " aria-hidden="true"  ></i>
                                    </button>
                                <button
                                    class="btn btn-link btn-icon icon-size-3 ml-1 mt-auto"
                                    aria-label="Отправить сообщение"
                                    data-action="send-message"
                                >
                                    <span data-region="send-icon-container"><i class="icon fa fa-paper-plane fa-fw " aria-hidden="true"  ></i></span>
                                    <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
</span>
                                </button>
                            </div>
                        </div>
                    </div>
                    <div class="hidden p-sm-2" data-region="content-messages-footer-edit-mode-container">

                        <div class="d-flex p-3 justify-content-end">
                            <button
                                class="btn btn-link btn-icon my-1 icon-size-4"
                                data-action="delete-selected-messages"
                                data-toggle="tooltip"
                                data-placement="top"
                                title="Удалить выбранные сообщения"
                            >
                                <span data-region="icon-container"><i class="icon fa fa-trash fa-fw " aria-hidden="true"  ></i></span>
                                <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
</span>
                                <span class="sr-only">Удалить выбранные сообщения</span>
                            </button>
                        </div>                    </div>
                    <div class="hidden bg-secondary p-sm-3" data-region="content-messages-footer-require-contact-container">

                        <div class="p-3 bg-white">
                            <p data-region="title"></p>
                            <p class="text-muted" data-region="text"></p>
                            <button type="button" class="btn btn-primary btn-block" data-action="request-add-contact">
                                <span data-region="dialogue-button-text">Отправить запрос на добавление в контакты</span>
                                <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
</span>
                            </button>
                        </div>
                    </div>
                    <div class="hidden bg-secondary p-sm-3" data-region="content-messages-footer-require-unblock-container">

                        <div class="p-3 bg-white">
                            <p class="text-muted" data-region="text">Вы заблокировали этого пользователя</p>
                            <button type="button" class="btn btn-primary btn-block" data-action="request-unblock">
                                <span data-region="dialogue-button-text">Разблокировать пользователя</span>
                                <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Загрузка" role="img" aria-label="Загрузка"></i></span>
</span>
                            </button>
                        </div>
                    </div>
                    <div class="hidden bg-secondary p-sm-3" data-region="content-messages-footer-unable-to-message">

                        <div class="p-3 bg-white">
                            <p class="text-muted" data-region="text">Вы не можете отправить сообщение этому пользователю</p>
                        </div>
                    </div>
                    <div class="p-sm-2" data-region="placeholder-container">
                        <div class="d-flex">
                            <div class="bg-pulse-grey w-100" style="height: 80px"></div>
                            <div class="mx-2 mb-2 align-self-end bg-pulse-grey" style="height: 20px; width: 20px"></div>
                        </div>                    </div>
                    <div
                        class="hidden position-absolute z-index-1"
                        data-region="confirm-dialogue-container"
                        style="top: -1px; bottom: 0; right: 0; left: 0; background: rgba(0,0,0,0.3);"
                    ></div>
                </div>                    <div data-region="view-overview" class="text-center">
                        <a href="https://edu.stankin.ru/message/index.php">
                            Смотреть все
                        </a>
                    </div>
            </div>
        </div>

</div>    </div>
</div>
<div class="clearfix"></div>
<div id="dock" role="menubar" aria-label="Блоки">
	<div class="buttons_container">
		<div class="dockeditem_container">
		    <div id="dock_item_0" class="dockeditem" aria-controls="inst4"><div id="dock_item_0_title" role="menu" aria-haspopup="true" class="dockedtitle" aria-expanded="false" 
	style="background-image:url('https://edu.stankin.ru/theme/image.php/opentechnology/block_navigation/1701486024/dock_icon_04');"><h2>Навигация</h2></div></div>
		</div>
	</div>
	<div id="dockeditempanel" class="dockitempanel_hidden">
		<div class="drop-here-message">Вы можете переместить блок сюда, чтобы он попал в док</div>
		<div class="dockeditempanel_content blockcolumn ">
        	<section data-region="blocks-column" class="d-print-none" aria-label="Блоки">		
		    <aside id="block-region-dock" class="block-region" data-blockregion="dock" data-droptarget="1"><a href="#sb-1" class="sr-only sr-only-focusable">Пропустить Навигация</a>

<section id="inst4"
     class=" block_navigation block  card mb-3"
     role="navigation"
     data-block="navigation"
     data-instance-id="4"
          aria-labelledby="instance-4-header"
     >

    <div class="card-body p-3">

            <h5 id="instance-4-header" class="card-title d-inline">Навигация</h5>


        <div class="card-text content mt-3">
            <ul class="block_tree list" role="tree" data-ajax-loader="block_navigation/nav_loader"><li class="type_unknown depth_1 contains_branch" role="treeitem" aria-expanded="true" aria-owns="random656b0a6ba1c2e2_group" data-collapsible="false" aria-labelledby="random656b0a6ba1c2e1_label_1_1"><p class="tree_item branch canexpand navigation_node"><a tabindex="-1" id="random656b0a6ba1c2e1_label_1_1" href="https://edu.stankin.ru/">В начало</a></p><ul id="random656b0a6ba1c2e2_group" role="group"><li class="type_setting depth_2 item_with_icon" role="treeitem" aria-labelledby="random656b0a6ba1c2e3_label_2_2"><p class="tree_item hasicon"><a tabindex="-1" id="random656b0a6ba1c2e3_label_2_2" href="https://edu.stankin.ru/my/"><i class="icon fa fa-tachometer fa-fw navicon" aria-hidden="true"  ></i><span class="item-content-wrap">Личный кабинет</span></a></p></li><li class="type_course depth_2 contains_branch" role="treeitem" aria-expanded="false" aria-owns="random656b0a6ba1c2e5_group" aria-labelledby="random656b0a6ba1c2e3_label_2_3"><p class="tree_item branch"><span tabindex="-1" id="random656b0a6ba1c2e3_label_2_3" title="Электронная образовательная среда ФГБОУ ВО &quot;МГТУ &quot;СТАНКИН&quot;">Страницы сайта</span></p><ul id="random656b0a6ba1c2e5_group" role="group" aria-hidden="true"><li class="type_custom depth_3 item_with_icon" role="treeitem" aria-labelledby="random656b0a6ba1c2e6_label_3_5"><p class="tree_item hasicon"><a tabindex="-1" id="random656b0a6ba1c2e6_label_3_5" href="https://edu.stankin.ru/my/courses.php"><i class="icon fa fa-square fa-fw navicon" aria-hidden="true"  ></i><span class="item-content-wrap">Мои курсы</span></a></p></li><li class="type_unknown depth_3 item_with_icon" role="treeitem" aria-labelledby="random656b0a6ba1c2e6_label_3_6"><p class="tree_item hasicon"><a tabindex="-1" id="random656b0a6ba1c2e6_label_3_6" href="https://edu.stankin.ru/blog/index.php"><i class="icon fa fa-square fa-fw navicon" aria-hidden="true"  ></i><span class="item-content-wrap">Блоги сайта</span></a></p></li><li class="type_custom depth_3 item_with_icon" role="treeitem" aria-labelledby="random656b0a6ba1c2e6_label_3_7"><p class="tree_item hasicon"><a tabindex="-1" id="random656b0a6ba1c2e6_label_3_7" href="https://edu.stankin.ru/badges/view.php?type=1"><i class="icon fa fa-square fa-fw navicon" aria-hidden="true"  ></i><span class="item-content-wrap">Значки сайта</span></a></p></li><li class="type_setting depth_3 item_with_icon" role="treeitem" aria-labelledby="random656b0a6ba1c2e6_label_3_8"><p class="tree_item hasicon"><a tabindex="-1" id="random656b0a6ba1c2e6_label_3_8" href="https://edu.stankin.ru/tag/search.php"><i class="icon fa fa-square fa-fw navicon" aria-hidden="true"  ></i><span class="item-content-wrap">Теги</span></a></p></li><li class="type_activity depth_3 item_with_icon" role="treeitem" aria-labelledby="random656b0a6ba1c2e6_label_3_12"><p class="tree_item hasicon"><a tabindex="-1" id="random656b0a6ba1c2e6_label_3_12" title="Гиперссылка" href="https://edu.stankin.ru/mod/url/view.php?id=198072"><img class="icon navicon" alt="Гиперссылка" title="Гиперссылка" src="https://edu.stankin.ru/theme/image.php/opentechnology/url/1701486024/monologo" /><span class="item-content-wrap">ОПРОС для обучающихся: цифровизация университета</span></a></p></li></ul></li><li class="type_system depth_2 contains_branch" role="treeitem" aria-expanded="true" aria-owns="random656b0a6ba1c2e12_group" aria-labelledby="random656b0a6ba1c2e3_label_2_13"><p class="tree_item branch"><a tabindex="-1" id="random656b0a6ba1c2e3_label_2_13" href="https://edu.stankin.ru/my/courses.php">Мои курсы</a></p><ul id="random656b0a6ba1c2e12_group" role="group"><li class="type_unknown depth_3 contains_branch" role="treeitem" aria-expanded="false" aria-owns="random656b0a6ba1c2e14_group" aria-labelledby="random656b0a6ba1c2e13_label_3_14"><p class="tree_item branch"><span tabindex="-1" id="random656b0a6ba1c2e13_label_3_14">Бакалавриат</span></p><ul id="random656b0a6ba1c2e14_group" role="group" aria-hidden="true"><li class="type_unknown depth_4 contains_branch" role="treeitem" aria-expanded="false" aria-owns="random656b0a6ba1c2e16_group" aria-labelledby="random656b0a6ba1c2e15_label_4_15"><p class="tree_item branch canexpand"><span tabindex="-1" id="random656b0a6ba1c2e15_label_4_15">Общие дисциплины</span></p><ul id="random656b0a6ba1c2e16_group" role="group" aria-hidden="true"><li class="type_course depth_5 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_8589" data-node-key="8589" data-node-type="20" aria-labelledby="random656b0a6ba1c2e17_label_5_16"><p class="tree_item branch" id="expandable_branch_20_8589"><a tabindex="-1" id="random656b0a6ba1c2e17_label_5_16" title="Прикладная физическая культура" href="https://edu.stankin.ru/course/view.php?id=8589">ПФК_1</a></p></li></ul></li></ul></li><li class="type_unknown depth_3 contains_branch" role="treeitem" aria-expanded="true" aria-owns="random656b0a6ba1c2e18_group" aria-labelledby="random656b0a6ba1c2e13_label_3_17"><p class="tree_item branch canexpand"><span tabindex="-1" id="random656b0a6ba1c2e13_label_3_17">Бакалавриат (ФГОС 3++)</span></p><ul id="random656b0a6ba1c2e18_group" role="group"><li class="type_unknown depth_4 contains_branch" role="treeitem" aria-expanded="false" aria-owns="random656b0a6ba1c2e20_group" aria-labelledby="random656b0a6ba1c2e19_label_4_18"><p class="tree_item branch canexpand"><span tabindex="-1" id="random656b0a6ba1c2e19_label_4_18">Общие дисциплины</span></p><ul id="random656b0a6ba1c2e20_group" role="group" aria-hidden="true"><li class="type_course depth_5 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_14132" data-node-key="14132" data-node-type="20" aria-labelledby="random656b0a6ba1c2e21_label_5_19"><p class="tree_item branch" id="expandable_branch_20_14132"><a tabindex="-1" id="random656b0a6ba1c2e21_label_5_19" title="Основы военной подготовки" href="https://edu.stankin.ru/course/view.php?id=14132">Основы военной подготовки(3++)</a></p></li><li class="type_course depth_5 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_12930" data-node-key="12930" data-node-type="20" aria-labelledby="random656b0a6ba1c2e21_label_5_20"><p class="tree_item branch" id="expandable_branch_20_12930"><a tabindex="-1" id="random656b0a6ba1c2e21_label_5_20" title="Экономика стартапа" href="https://edu.stankin.ru/course/view.php?id=12930">Экономика стартапа (3++)</a></p></li><li class="type_course depth_5 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_12887" data-node-key="12887" data-node-type="20" aria-labelledby="random656b0a6ba1c2e21_label_5_21"><p class="tree_item branch" id="expandable_branch_20_12887"><a tabindex="-1" id="random656b0a6ba1c2e21_label_5_21" title="Прикладная физическая культура (Интеллектуальные виды спорта)" href="https://edu.stankin.ru/course/view.php?id=12887">Прикладная физическая культура (Интеллектуальные в...</a></p></li><li class="type_course depth_5 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_12886" data-node-key="12886" data-node-type="20" aria-labelledby="random656b0a6ba1c2e21_label_5_22"><p class="tree_item branch" id="expandable_branch_20_12886"><a tabindex="-1" id="random656b0a6ba1c2e21_label_5_22" title="Прикладная физическая культура (Спортивные игры)" href="https://edu.stankin.ru/course/view.php?id=12886">Прикладная физическая культура (Спортивные игры) (++)</a></p></li><li class="type_course depth_5 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_11920" data-node-key="11920" data-node-type="20" aria-labelledby="random656b0a6ba1c2e21_label_5_23"><p class="tree_item branch" id="expandable_branch_20_11920"><a tabindex="-1" id="random656b0a6ba1c2e21_label_5_23" title="Введение в проектную деятельность" href="https://edu.stankin.ru/course/view.php?id=11920">Введение в проектную деятельность</a></p></li><li class="type_course depth_5 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_11912" data-node-key="11912" data-node-type="20" aria-labelledby="random656b0a6ba1c2e21_label_5_24"><p class="tree_item branch" id="expandable_branch_20_11912"><a tabindex="-1" id="random656b0a6ba1c2e21_label_5_24" title="История (всеобщая история, история России)" href="https://edu.stankin.ru/course/view.php?id=11912">История (всеобщая история, история России)</a></p></li><li class="type_course depth_5 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_10954" data-node-key="10954" data-node-type="20" aria-labelledby="random656b0a6ba1c2e21_label_5_25"><p class="tree_item branch" id="expandable_branch_20_10954"><a tabindex="-1" id="random656b0a6ba1c2e21_label_5_25" title="Прикладная физическая культура" href="https://edu.stankin.ru/course/view.php?id=10954">Прикл. ФК (++)</a></p></li><li class="type_course depth_5 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_11918" data-node-key="11918" data-node-type="20" aria-labelledby="random656b0a6ba1c2e21_label_5_26"><p class="tree_item branch" id="expandable_branch_20_11918"><a tabindex="-1" id="random656b0a6ba1c2e21_label_5_26" title="Психология и педагогика" href="https://edu.stankin.ru/course/view.php?id=11918">Психология и педагогика</a></p></li><li class="type_course depth_5 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_11915" data-node-key="11915" data-node-type="20" aria-labelledby="random656b0a6ba1c2e21_label_5_27"><p class="tree_item branch" id="expandable_branch_20_11915"><a tabindex="-1" id="random656b0a6ba1c2e21_label_5_27" title="Русский язык и речевое поведение" href="https://edu.stankin.ru/course/view.php?id=11915">Русский язык и речевое поведение</a></p></li><li class="type_course depth_5 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_11922" data-node-key="11922" data-node-type="20" aria-labelledby="random656b0a6ba1c2e21_label_5_28"><p class="tree_item branch" id="expandable_branch_20_11922"><a tabindex="-1" id="random656b0a6ba1c2e21_label_5_28" title="Технологии индустрии 4.0" href="https://edu.stankin.ru/course/view.php?id=11922">Технологии индустрии 4.0</a></p></li><li class="type_course depth_5 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_12181" data-node-key="12181" data-node-type="20" aria-labelledby="random656b0a6ba1c2e21_label_5_29"><p class="tree_item branch" id="expandable_branch_20_12181"><a tabindex="-1" id="random656b0a6ba1c2e21_label_5_29" title="Траектория обучения и личностного развития" href="https://edu.stankin.ru/course/view.php?id=12181">Траектория обучения и личностного развития (++)</a></p></li><li class="type_course depth_5 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_10945" data-node-key="10945" data-node-type="20" aria-labelledby="random656b0a6ba1c2e21_label_5_30"><p class="tree_item branch" id="expandable_branch_20_10945"><a tabindex="-1" id="random656b0a6ba1c2e21_label_5_30" title="Физика" href="https://edu.stankin.ru/course/view.php?id=10945">Физика (++)</a></p></li><li class="type_course depth_5 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_10943" data-node-key="10943" data-node-type="20" aria-labelledby="random656b0a6ba1c2e21_label_5_31"><p class="tree_item branch" id="expandable_branch_20_10943"><a tabindex="-1" id="random656b0a6ba1c2e21_label_5_31" title="Физическая культура и спорт" href="https://edu.stankin.ru/course/view.php?id=10943">ФК и спорт (++)</a></p></li><li class="type_course depth_5 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_10940" data-node-key="10940" data-node-type="20" aria-labelledby="random656b0a6ba1c2e21_label_5_32"><p class="tree_item branch" id="expandable_branch_20_10940"><a tabindex="-1" id="random656b0a6ba1c2e21_label_5_32" title="Философия" href="https://edu.stankin.ru/course/view.php?id=10940">Фил. (++)</a></p></li></ul></li><li class="type_unknown depth_4 contains_branch" role="treeitem" aria-expanded="true" aria-owns="random656b0a6ba1c2e22_group" aria-labelledby="random656b0a6ba1c2e19_label_4_33"><p class="tree_item branch canexpand"><span tabindex="-1" id="random656b0a6ba1c2e19_label_4_33">УГСН 09.00.00 (ФГОС 3++)</span></p><ul id="random656b0a6ba1c2e22_group" role="group"><li class="type_unknown depth_5 contains_branch" role="treeitem" aria-expanded="true" aria-owns="random656b0a6ba1c2e24_group" aria-labelledby="random656b0a6ba1c2e23_label_5_34"><p class="tree_item branch canexpand"><span tabindex="-1" id="random656b0a6ba1c2e23_label_5_34">Общие дисциплины (09 группа)</span></p><ul id="random656b0a6ba1c2e24_group" role="group"><li class="type_course depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_13311" data-node-key="13311" data-node-type="20" aria-labelledby="random656b0a6ba1c2e25_label_6_35"><p class="tree_item branch" id="expandable_branch_20_13311"><a tabindex="-1" id="random656b0a6ba1c2e25_label_6_35" title="Безопасность жизнедеятельности" href="https://edu.stankin.ru/course/view.php?id=13311">Безопасность жизнедеятельности09++</a></p></li><li class="type_course depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_10949" data-node-key="10949" data-node-type="20" aria-labelledby="random656b0a6ba1c2e25_label_6_36"><p class="tree_item branch" id="expandable_branch_20_10949"><a tabindex="-1" id="random656b0a6ba1c2e25_label_6_36" title="Дискретная математика" href="https://edu.stankin.ru/course/view.php?id=10949">Дискр. мат. (09++)</a></p></li><li class="type_course depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_10941" data-node-key="10941" data-node-type="20" aria-labelledby="random656b0a6ba1c2e25_label_6_37"><p class="tree_item branch" id="expandable_branch_20_10941"><a tabindex="-1" id="random656b0a6ba1c2e25_label_6_37" title="Иностранный язык" href="https://edu.stankin.ru/course/view.php?id=10941">Ин. язык (09++)</a></p></li><li class="type_course depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_10944" data-node-key="10944" data-node-type="20" aria-labelledby="random656b0a6ba1c2e25_label_6_38"><p class="tree_item branch" id="expandable_branch_20_10944"><a tabindex="-1" id="random656b0a6ba1c2e25_label_6_38" title="Математический анализ" href="https://edu.stankin.ru/course/view.php?id=10944">Мат. анализ (09.03.02-03++)</a></p></li><li class="type_course depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_10947" data-node-key="10947" data-node-type="20" aria-labelledby="random656b0a6ba1c2e25_label_6_39"><p class="tree_item branch" id="expandable_branch_20_10947"><a tabindex="-1" id="random656b0a6ba1c2e25_label_6_39" title="Операционные системы" href="https://edu.stankin.ru/course/view.php?id=10947">ОС (09++)</a></p></li><li class="type_course depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_10952" data-node-key="10952" data-node-type="20" aria-labelledby="random656b0a6ba1c2e25_label_6_40"><p class="tree_item branch" id="expandable_branch_20_10952"><a tabindex="-1" id="random656b0a6ba1c2e25_label_6_40" title="Теория вероятностей, математическая статистика и случайные процессы" href="https://edu.stankin.ru/course/view.php?id=10952">Теор. вер. (09++)</a></p></li><li class="type_course depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_11070" data-node-key="11070" data-node-type="20" aria-labelledby="random656b0a6ba1c2e25_label_6_41"><p class="tree_item branch" id="expandable_branch_20_11070"><a tabindex="-1" id="random656b0a6ba1c2e25_label_6_41" title="Электротехника" href="https://edu.stankin.ru/course/view.php?id=11070">Электротехника (09++)</a></p></li><li class="type_course depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_11068" data-node-key="11068" data-node-type="20" aria-labelledby="random656b0a6ba1c2e25_label_6_42"><p class="tree_item branch" id="expandable_branch_20_11068"><a tabindex="-1" id="random656b0a6ba1c2e25_label_6_42" title="Технические средства информационных систем" href="https://edu.stankin.ru/course/view.php?id=11068">ТСИС (090303++)</a></p></li><li class="type_course depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_11066" data-node-key="11066" data-node-type="20" aria-labelledby="random656b0a6ba1c2e25_label_6_43"><p class="tree_item branch" id="expandable_branch_20_11066"><a tabindex="-1" id="random656b0a6ba1c2e25_label_6_43" title="Теория систем и системный анализ" href="https://edu.stankin.ru/course/view.php?id=11066">ТССА (090303++)</a></p></li><li class="type_course depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_11065" data-node-key="11065" data-node-type="20" aria-labelledby="random656b0a6ba1c2e25_label_6_44"><p class="tree_item branch" id="expandable_branch_20_11065"><a tabindex="-1" id="random656b0a6ba1c2e25_label_6_44" title="Теория графов и тензорное исчисление" href="https://edu.stankin.ru/course/view.php?id=11065">ТГТИ (090303++)</a></p></li><li class="type_course depth_6 contains_branch" role="treeitem" aria-expanded="true" aria-owns="random656b0a6ba1c2e26_group" aria-labelledby="random656b0a6ba1c2e25_label_6_45"><p class="tree_item branch canexpand"><a tabindex="-1" id="random656b0a6ba1c2e25_label_6_45" title="Прикладное программирование" href="https://edu.stankin.ru/course/view.php?id=11060">Прикл. прогр. (090303++)</a></p><ul id="random656b0a6ba1c2e26_group" role="group"><li class="type_container depth_7 contains_branch" role="treeitem" aria-expanded="false" aria-owns="random656b0a6ba1c2e28_group" aria-labelledby="random656b0a6ba1c2e27_label_7_46"><p class="tree_item branch"><a tabindex="-1" id="random656b0a6ba1c2e27_label_7_46" href="https://edu.stankin.ru/user/index.php?id=11060">Участники</a></p><ul id="random656b0a6ba1c2e28_group" role="group" aria-hidden="true"><li class="type_setting depth_8 item_with_icon" role="treeitem" aria-labelledby="random656b0a6ba1c2e29_label_8_47"><p class="tree_item hasicon"><a tabindex="-1" id="random656b0a6ba1c2e29_label_8_47" href="https://edu.stankin.ru/blog/index.php?groupid=10109"><i class="icon fa fa-square fa-fw navicon" aria-hidden="true"  ></i><span class="item-content-wrap">Блоги курса</span></a></p></li><li class="type_user depth_8 item_with_icon" role="treeitem" aria-labelledby="random656b0a6ba1c2e29_label_8_48"><p class="tree_item hasicon"><a tabindex="-1" id="random656b0a6ba1c2e29_label_8_48" href="https://edu.stankin.ru/user/view.php?id=24186&amp;course=11060"><i class="icon fa fa-square fa-fw navicon" aria-hidden="true"  ></i><span class="item-content-wrap">Потачин Владислав Николаевич</span></a></p></li></ul></li><li class="type_setting depth_7 item_with_icon" role="treeitem" aria-labelledby="random656b0a6ba1c2e27_label_7_49"><p class="tree_item hasicon"><a tabindex="-1" id="random656b0a6ba1c2e27_label_7_49" href="https://edu.stankin.ru/admin/tool/lp/coursecompetencies.php?courseid=11060"><i class="icon fa fa-check-square-o fa-fw navicon" aria-hidden="true"  ></i><span class="item-content-wrap">Компетенции</span></a></p></li><li class="type_setting depth_7 item_with_icon" role="treeitem" aria-labelledby="random656b0a6ba1c2e27_label_7_50"><p class="tree_item hasicon"><a tabindex="-1" id="random656b0a6ba1c2e27_label_7_50" href="https://edu.stankin.ru/grade/report/index.php?id=11060"><i class="icon fa fa-table fa-fw navicon" aria-hidden="true"  ></i><span class="item-content-wrap">Оценки</span></a></p></li><li class="type_structure depth_7 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_30_47964" data-node-key="47964" data-node-type="30" aria-labelledby="random656b0a6ba1c2e27_label_7_51"><p class="tree_item branch" id="expandable_branch_30_47964"><span tabindex="-1" id="random656b0a6ba1c2e27_label_7_51">Общее</span></p></li><li class="type_structure depth_7 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_30_56593" data-node-key="56593" data-node-type="30" aria-labelledby="random656b0a6ba1c2e27_label_7_52"><p class="tree_item branch" id="expandable_branch_30_56593"><span tabindex="-1" id="random656b0a6ba1c2e27_label_7_52">Раздел 1. Введение</span></p></li><li class="type_structure depth_7 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_30_56594" data-node-key="56594" data-node-type="30" aria-labelledby="random656b0a6ba1c2e27_label_7_53"><p class="tree_item branch" id="expandable_branch_30_56594"><span tabindex="-1" id="random656b0a6ba1c2e27_label_7_53">Раздел 2. Обработка ошибок</span></p></li><li class="type_structure depth_7 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_30_56596" data-node-key="56596" data-node-type="30" aria-labelledby="random656b0a6ba1c2e27_label_7_54"><p class="tree_item branch" id="expandable_branch_30_56596"><span tabindex="-1" id="random656b0a6ba1c2e27_label_7_54">Раздел 4. Приложения с графическим интерфейсом</span></p></li><li class="type_structure depth_7 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_30_56597" data-node-key="56597" data-node-type="30" aria-labelledby="random656b0a6ba1c2e27_label_7_55"><p class="tree_item branch" id="expandable_branch_30_56597"><span tabindex="-1" id="random656b0a6ba1c2e27_label_7_55">Раздел 5. Принципы SOLID</span></p></li><li class="type_structure depth_7 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_30_56598" data-node-key="56598" data-node-type="30" aria-labelledby="random656b0a6ba1c2e27_label_7_56"><p class="tree_item branch" id="expandable_branch_30_56598"><span tabindex="-1" id="random656b0a6ba1c2e27_label_7_56">Раздел 6. Системы контроля версий</span></p></li><li class="type_structure depth_7 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_30_89708" data-node-key="89708" data-node-type="30" aria-labelledby="random656b0a6ba1c2e27_label_7_57"><p class="tree_item branch" id="expandable_branch_30_89708"><span tabindex="-1" id="random656b0a6ba1c2e27_label_7_57">Раздел 7. Стандартная библиотека шаблонов (STL)</span></p></li><li class="type_structure depth_7 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_30_89709" data-node-key="89709" data-node-type="30" aria-labelledby="random656b0a6ba1c2e27_label_7_58"><p class="tree_item branch" id="expandable_branch_30_89709"><span tabindex="-1" id="random656b0a6ba1c2e27_label_7_58">Раздел 8. Работа с данными</span></p></li><li class="type_structure depth_7 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_30_47966" data-node-key="47966" data-node-type="30" aria-labelledby="random656b0a6ba1c2e27_label_7_59"><p class="tree_item branch" id="expandable_branch_30_47966"><span tabindex="-1" id="random656b0a6ba1c2e27_label_7_59">Литература</span></p></li><li class="type_structure depth_7 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_30_47967" data-node-key="47967" data-node-type="30" aria-labelledby="random656b0a6ba1c2e27_label_7_60"><p class="tree_item branch" id="expandable_branch_30_47967"><span tabindex="-1" id="random656b0a6ba1c2e27_label_7_60">Экзамен (зачет)</span></p></li><li class="type_structure depth_7 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_30_94139" data-node-key="94139" data-node-type="30" aria-labelledby="random656b0a6ba1c2e27_label_7_61"><p class="tree_item branch" id="expandable_branch_30_94139"><span tabindex="-1" id="random656b0a6ba1c2e27_label_7_61">ИДБ-22-11</span></p></li><li class="type_structure depth_7 contains_branch" role="treeitem" aria-expanded="true" aria-owns="random656b0a6ba1c2e34_group" aria-labelledby="random656b0a6ba1c2e27_label_7_62"><p class="tree_item branch"><span tabindex="-1" id="random656b0a6ba1c2e27_label_7_62">Лабораторные работы</span></p><ul id="random656b0a6ba1c2e34_group" role="group"><li class="type_activity depth_8 item_with_icon" role="treeitem" aria-labelledby="random656b0a6ba1c2e35_label_8_63"><p class="tree_item hasicon"><a tabindex="-1" id="random656b0a6ba1c2e35_label_8_63" title="Задание" href="https://edu.stankin.ru/mod/assign/view.php?id=376884"><img class="icon navicon" alt="Задание" title="Задание" src="https://edu.stankin.ru/theme/image.php/opentechnology/assign/1701486024/monologo" /><span class="item-content-wrap">Лабораторная работа № 1 «ООП в Python. Обработка и...</span></a></p></li><li class="type_activity depth_8 item_with_icon" role="treeitem" aria-labelledby="random656b0a6ba1c2e35_label_8_64"><p class="tree_item hasicon"><a tabindex="-1" id="random656b0a6ba1c2e35_label_8_64" title="Задание" href="https://edu.stankin.ru/mod/assign/view.php?id=379455"><img class="icon navicon" alt="Задание" title="Задание" src="https://edu.stankin.ru/theme/image.php/opentechnology/assign/1701486024/monologo" /><span class="item-content-wrap">Лабораторная работа № 2 «Python: оконные приложени...</span></a></p></li><li class="type_activity depth_8 item_with_icon current_branch" role="treeitem" aria-labelledby="random656b0a6ba1c2e35_label_8_65"><p class="tree_item hasicon active_tree_node"><a tabindex="-1" id="random656b0a6ba1c2e35_label_8_65" title="Задание" href="https://edu.stankin.ru/mod/assign/view.php?id=380903"><img class="icon navicon" alt="Задание" title="Задание" src="https://edu.stankin.ru/theme/image.php/opentechnology/assign/1701486024/monologo" /><span class="item-content-wrap">Лабораторная работа № 3 «Регулярные выражения. Раб...</span></a></p></li><li class="type_activity depth_8 item_with_icon" role="treeitem" aria-labelledby="random656b0a6ba1c2e35_label_8_66"><p class="tree_item hasicon"><a tabindex="-1" id="random656b0a6ba1c2e35_label_8_66" title="Задание" href="https://edu.stankin.ru/mod/assign/view.php?id=380904"><img class="icon navicon" alt="Задание" title="Задание" src="https://edu.stankin.ru/theme/image.php/opentechnology/assign/1701486024/monologo" /><span class="item-content-wrap">Лабораторная работа № 4 «Анализ данных. Работа с A...</span></a></p></li></ul></li><li class="type_structure depth_7 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_30_94446" data-node-key="94446" data-node-type="30" aria-labelledby="random656b0a6ba1c2e27_label_7_67"><p class="tree_item branch" id="expandable_branch_30_94446"><span tabindex="-1" id="random656b0a6ba1c2e27_label_7_67">Семинары ИДБ-22-12, ИДБ-22-13</span></p></li></ul></li><li class="type_course depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_11059" data-node-key="11059" data-node-type="20" aria-labelledby="random656b0a6ba1c2e25_label_6_68"><p class="tree_item branch" id="expandable_branch_20_11059"><a tabindex="-1" id="random656b0a6ba1c2e25_label_6_68" title="Основы программирования" href="https://edu.stankin.ru/course/view.php?id=11059">Осн. прогр. (090303++)</a></p></li><li class="type_course depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_11058" data-node-key="11058" data-node-type="20" aria-labelledby="random656b0a6ba1c2e25_label_6_69"><p class="tree_item branch" id="expandable_branch_20_11058"><a tabindex="-1" id="random656b0a6ba1c2e25_label_6_69" title="Начертательная геометрия" href="https://edu.stankin.ru/course/view.php?id=11058">Начертательная геометрия (09++)</a></p></li><li class="type_course depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_11056" data-node-key="11056" data-node-type="20" aria-labelledby="random656b0a6ba1c2e25_label_6_70"><p class="tree_item branch" id="expandable_branch_20_11056"><a tabindex="-1" id="random656b0a6ba1c2e25_label_6_70" title="Модели и методы теории вычислений" href="https://edu.stankin.ru/course/view.php?id=11056">ММТВ (090303++)</a></p></li><li class="type_course depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_11048" data-node-key="11048" data-node-type="20" aria-labelledby="random656b0a6ba1c2e25_label_6_71"><p class="tree_item branch" id="expandable_branch_20_11048"><a tabindex="-1" id="random656b0a6ba1c2e25_label_6_71" title="Вычислительные системы, сети и телекоммуникации" href="https://edu.stankin.ru/course/view.php?id=11048">ВССТ (090303++)</a></p></li><li class="type_course depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_11047" data-node-key="11047" data-node-type="20" aria-labelledby="random656b0a6ba1c2e25_label_6_72"><p class="tree_item branch" id="expandable_branch_20_11047"><a tabindex="-1" id="random656b0a6ba1c2e25_label_6_72" title="Алгоритмы и структуры данных" href="https://edu.stankin.ru/course/view.php?id=11047">АиСД (090303++)</a></p></li><li class="type_course depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_10971" data-node-key="10971" data-node-type="20" aria-labelledby="random656b0a6ba1c2e25_label_6_73"><p class="tree_item branch" id="expandable_branch_20_10971"><a tabindex="-1" id="random656b0a6ba1c2e25_label_6_73" title="Объектно-ориентированное программирование" href="https://edu.stankin.ru/course/view.php?id=10971">ООП (090303++)</a></p></li><li class="type_course depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_10966" data-node-key="10966" data-node-type="20" aria-labelledby="random656b0a6ba1c2e25_label_6_74"><p class="tree_item branch" id="expandable_branch_20_10966"><a tabindex="-1" id="random656b0a6ba1c2e25_label_6_74" title="Базы данных" href="https://edu.stankin.ru/course/view.php?id=10966">БД (090303++)</a></p></li></ul></li><li class="type_unknown depth_5 contains_branch" role="treeitem" aria-expanded="false" aria-owns="random656b0a6ba1c2e40_group" aria-labelledby="random656b0a6ba1c2e23_label_5_75"><p class="tree_item branch canexpand"><span tabindex="-1" id="random656b0a6ba1c2e23_label_5_75">09.03.03 Прикладная информатика (ФГОС 3++)</span></p><ul id="random656b0a6ba1c2e40_group" role="group" aria-hidden="true"><li class="type_course depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_13927" data-node-key="13927" data-node-type="20" aria-labelledby="random656b0a6ba1c2e41_label_6_76"><p class="tree_item branch" id="expandable_branch_20_13927"><a tabindex="-1" id="random656b0a6ba1c2e41_label_6_76" title="Дифференциальные уравнения и ряды" href="https://edu.stankin.ru/course/view.php?id=13927">Дифференциальные уравнения и ряды(09.03.03++)</a></p></li><li class="type_course depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_10976" data-node-key="10976" data-node-type="20" aria-labelledby="random656b0a6ba1c2e41_label_6_77"><p class="tree_item branch" id="expandable_branch_20_10976"><a tabindex="-1" id="random656b0a6ba1c2e41_label_6_77" title="Введение в специальность" href="https://edu.stankin.ru/course/view.php?id=10976">Введ. в спец. (090303++)</a></p></li><li class="type_course depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_11051" data-node-key="11051" data-node-type="20" aria-labelledby="random656b0a6ba1c2e41_label_6_78"><p class="tree_item branch" id="expandable_branch_20_11051"><a tabindex="-1" id="random656b0a6ba1c2e41_label_6_78" title="Инновационные технологии цифрового производства" href="https://edu.stankin.ru/course/view.php?id=11051">ИТЦП (090303++)</a></p></li><li class="type_course depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_11054" data-node-key="11054" data-node-type="20" aria-labelledby="random656b0a6ba1c2e41_label_6_79"><p class="tree_item branch" id="expandable_branch_20_11054"><a tabindex="-1" id="random656b0a6ba1c2e41_label_6_79" title="Компьютерная механика" href="https://edu.stankin.ru/course/view.php?id=11054">КМ (090303++)</a></p></li><li class="type_course depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_11139" data-node-key="11139" data-node-type="20" aria-labelledby="random656b0a6ba1c2e41_label_6_80"><p class="tree_item branch" id="expandable_branch_20_11139"><a tabindex="-1" id="random656b0a6ba1c2e41_label_6_80" title="Учебная практика (ознакомительная)" href="https://edu.stankin.ru/course/view.php?id=11139">Уч. пр-ка (09.03.03++)</a></p></li></ul></li><li class="type_course depth_5 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_10963" data-node-key="10963" data-node-type="20" aria-labelledby="random656b0a6ba1c2e23_label_5_81"><p class="tree_item branch" id="expandable_branch_20_10963"><a tabindex="-1" id="random656b0a6ba1c2e23_label_5_81" title="Информатика" href="https://edu.stankin.ru/course/view.php?id=10963">Информатика_090303_090304-РиСПО (++)</a></p></li><li class="type_course depth_5 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_13926" data-node-key="13926" data-node-type="20" aria-labelledby="random656b0a6ba1c2e23_label_5_82"><p class="tree_item branch" id="expandable_branch_20_13926"><a tabindex="-1" id="random656b0a6ba1c2e23_label_5_82" title="Линейная алгебра и аналитическая геометрия" href="https://edu.stankin.ru/course/view.php?id=13926">Линейная алгебра и аналитическая геометрия_09.03.0...</a></p></li></ul></li><li class="type_course depth_4 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_14162" data-node-key="14162" data-node-type="20" aria-labelledby="random656b0a6ba1c2e19_label_4_83"><p class="tree_item branch" id="expandable_branch_20_14162"><a tabindex="-1" id="random656b0a6ba1c2e19_label_4_83" title="Технологии виртуальной реальности в машиностроении " href="https://edu.stankin.ru/course/view.php?id=14162">ТехнVRвМаш23</a></p></li></ul></li><li class="type_unknown depth_3 contains_branch" role="treeitem" aria-expanded="false" aria-owns="random656b0a6ba1c2e42_group" aria-labelledby="random656b0a6ba1c2e13_label_3_84"><p class="tree_item branch canexpand"><span tabindex="-1" id="random656b0a6ba1c2e13_label_3_84">Разное</span></p><ul id="random656b0a6ba1c2e42_group" role="group" aria-hidden="true"><li class="type_course depth_4 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_11642" data-node-key="11642" data-node-type="20" aria-labelledby="random656b0a6ba1c2e43_label_4_85"><p class="tree_item branch" id="expandable_branch_20_11642"><a tabindex="-1" id="random656b0a6ba1c2e43_label_4_85" title="Анкетирование студентов" href="https://edu.stankin.ru/course/view.php?id=11642">Анкетирование студентов</a></p></li><li class="type_course depth_4 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_8104" data-node-key="8104" data-node-type="20" aria-labelledby="random656b0a6ba1c2e43_label_4_86"><p class="tree_item branch" id="expandable_branch_20_8104"><a tabindex="-1" id="random656b0a6ba1c2e43_label_4_86" title="Портфолио" href="https://edu.stankin.ru/course/view.php?id=8104">Портфолио</a></p></li></ul></li><li class="type_unknown depth_3 contains_branch" role="treeitem" aria-expanded="false" aria-owns="random656b0a6ba1c2e44_group" aria-labelledby="random656b0a6ba1c2e13_label_3_87"><p class="tree_item branch canexpand"><span tabindex="-1" id="random656b0a6ba1c2e13_label_3_87">Массовые открытые онлайн-курсы</span></p><ul id="random656b0a6ba1c2e44_group" role="group" aria-hidden="true"><li class="type_course depth_4 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_9203" data-node-key="9203" data-node-type="20" aria-labelledby="random656b0a6ba1c2e45_label_4_88"><p class="tree_item branch" id="expandable_branch_20_9203"><a tabindex="-1" id="random656b0a6ba1c2e45_label_4_88" title="Противодействие идеологии экстремизма и терроризма" href="https://edu.stankin.ru/course/view.php?id=9203">Антитеррор</a></p></li></ul></li><li class="type_unknown depth_3 contains_branch" role="treeitem" aria-expanded="false" aria-owns="random656b0a6ba1c2e46_group" aria-labelledby="random656b0a6ba1c2e13_label_3_89"><p class="tree_item branch canexpand"><span tabindex="-1" id="random656b0a6ba1c2e13_label_3_89">Гостевой доступ</span></p><ul id="random656b0a6ba1c2e46_group" role="group" aria-hidden="true"><li class="type_course depth_4 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_20_11557" data-node-key="11557" data-node-type="20" aria-labelledby="random656b0a6ba1c2e47_label_4_90"><p class="tree_item branch" id="expandable_branch_20_11557"><a tabindex="-1" id="random656b0a6ba1c2e47_label_4_90" title="Расписание занятий" href="https://edu.stankin.ru/course/view.php?id=11557">Расписание</a></p></li></ul></li></ul></li><li class="type_system depth_2 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_0_courses" data-node-key="courses" data-node-type="0" aria-labelledby="random656b0a6ba1c2e3_label_2_91"><p class="tree_item branch" id="expandable_branch_0_courses"><a tabindex="-1" id="random656b0a6ba1c2e3_label_2_91" href="https://edu.stankin.ru/local/crw/">Курсы</a></p></li></ul></li></ul>
            <div class="footer"></div>

        </div>

    </div>

</section>

  <span id="sb-1"></span></aside>
		    </section>
		</div>
	</div>
</div><div id="blocks-content-footing-wrapper">
    <div id="blocks-content-footing-position" class="container-fluid ">
        <aside id="block-region-content-footing" class=" block-region" data-blockregion="content-footing" data-droptarget="1"></aside>    </div>
</div>
<footer id="page-footer" class="moodle-has-zindex">
    <div data-region="footer-container-popover">
        <button class="btn btn-icon btn-secondary icon-no-margin btn-footer-popover" data-action="footer-popover" aria-label="Показать нижний колонтитул">
            <i class="icon fa fa-question fa-fw " aria-hidden="true"  ></i>
        </button>
    </div>
    <div class="footer-content-popover container" data-region="footer-content-popover" data-popovercontent='<div class="footer-section footer-section-support px-4 pt-3 pb-0">
    <div class="otsupport" id="ot-support-footer-656b0a6baeda7"></div>
        <div class="footer-support-link pt-1"><a href="https://edu.stankin.ru/user/contactsitesupport.php">Служба поддержки сайта</a></div>
    <div class="mw-75 border-bottom pb-2"></div>
</div>
<div class="footer-section footer-section-loginfo px-4 pb-0">
    <div class="logininfo pb-0">
        <div class="logininfo">Вы зашли под именем <a href="https://edu.stankin.ru/user/profile.php?id=24186" title="Просмотр профиля">Потачин Владислав Николаевич</a> (<a href="https://edu.stankin.ru/login/logout.php?sesskey=0ldtSfBaXr">Выход</a>)</div>
    </div>
    <div class="tool_usertours-resettourcontainer pb-1" >
    </div>
    <div class="tool_dataprivacy"><a href="https://edu.stankin.ru/admin/tool/dataprivacy/summary.php">Сводка хранения данных</a></div><a class="mobilelink" href="https://download.moodle.org/mobile?version=2022112805&amp;lang=ru&amp;iosappid=633359593&amp;androidappid=com.moodle.moodlemobile">Скачать мобильное приложение</a>
    <div class="mw-75 border-bottom pb-3"></div>
</div>
<div class="footer-section footer-section-platform px-4 py-3">
        <div>На платформе <a href="http://opentechnology.ru/products/russianmoodle">CЭО 3KL</a></div>
        <div>
            Версия 4.1.5c (2023083003)
        </div>
</div>'>\
    <div class="tool_usertours-resettourcontainer"></div>
    </div>
	<div class="footerborder-wrapper">
		<div class="footerborder container-fluid "></div>
	</div>
	<div class="footer-content-wrapper">
    	<div class="container-fluid ">
        	<div id="footer_wrapper" class="footer_wrapper moodle-has-zindex">
           		<div id="footer_content" class="row">
                    <div id="f_leftblock_wrapper" class="f_logo_wrapper col-md-1 desktop-first-column">
                   		<div id="f_logo_wrapper">

                   		</div>
                   		<div id="f_logo_text">
                   	   		<div class="footer_logoimage_text"><p><a href="https://stankin.ru/">Официальный&nbsp;сайт</a><br></p></div>
                   	   	</div>
                   	   	<div id="f_social_wrapper">
                   	   		<div class="social_block"><div class="social_blocklinks"><a class="vkontakte btn btn-primary p-0" href="https://vk.com/msut_stankin
"></a></div></div>
                   	   	</div>
                   	   	<div class="clearfix"></div>
                   	</div>
                   	<div id="f_centerblock_wrapper" class="col-md-7">
                   		<div id="f_text_wrapper">

                   	   	</div>
                   	</div>
                   	<div id="f_rightblock_wrapper" class="col-md-4 desktop-last-column">
                   		<div id="logininfo_wrapper" class="logininfo_wrapper">
                            <div class="logininfo">Вы зашли под именем <a href="https://edu.stankin.ru/user/profile.php?id=24186" class="btn btn-link" title="Просмотр профиля">Владислав Николаевич Потачин</a> <a href="https://edu.stankin.ru/login/logout.php?sesskey=0ldtSfBaXr" class="btn button btn-primary">Выход</a></div>
                        </div>
                       	<div id="copyright_wrapper" class="copyright_wrapper row">
                       		<div id="copyright" class="pull-right col-md-12 desktop-last-column">
                           		<div class="f_copyright_text"><div class="f_copyright_text_content"><p>Все права защищены © 2023 ФГБОУ ВО «МГТУ «СТАНКИН»<br></p></div></div>
                       		</div>
                       	</div>
                       	<div id="rm3kl">
                           	<a href="http://opentechnology.ru/products/russianmoodle">На базе СЭО 3KL</a>
                        </div>
                   	</div>
                   	<div class="systeminfo col-md-12">
                       	<div class="tool_dataprivacy"><a href="https://edu.stankin.ru/admin/tool/dataprivacy/summary.php">Сводка хранения данных</a></div><a class="mobilelink" href="https://download.moodle.org/mobile?version=2022112805&amp;lang=ru&amp;iosappid=633359593&amp;androidappid=com.moodle.moodlemobile">Скачать мобильное приложение</a>
                    </div>
           		</div>
        	</div>
    	</div>
	</div>
<div class="footer-content-debugging">
    <div class="container-fluid">

    </div>
</div>
</footer>
<script>
//<![CDATA[
var require = {
    baseUrl : 'https://edu.stankin.ru/lib/requirejs.php/1701486024/',
    // We only support AMD modules with an explicit define() statement.
    enforceDefine: true,
    skipDataMain: true,
    waitSeconds : 0,

    paths: {
        jquery: 'https://edu.stankin.ru/lib/javascript.php/1701486024/lib/jquery/jquery-3.6.1.min',
        jqueryui: 'https://edu.stankin.ru/lib/javascript.php/1701486024/lib/jquery/ui-1.13.2/jquery-ui.min',
        jqueryprivate: 'https://edu.stankin.ru/lib/javascript.php/1701486024/lib/requirejs/jquery-private'
    },

    // Custom jquery config map.
    map: {
      // '*' means all modules will get 'jqueryprivate'
      // for their 'jquery' dependency.
      '*': { jquery: 'jqueryprivate' },
      // Stub module for 'process'. This is a workaround for a bug in MathJax (see MDL-60458).
      '*': { process: 'core/first' },

      // 'jquery-private' wants the real jQuery module
      // though. If this line was not here, there would
      // be an unresolvable cyclic dependency.
      jqueryprivate: { jquery: 'jquery' }
    }
};

//]]>
</script>
<script src="https://edu.stankin.ru/lib/javascript.php/1701486024/lib/requirejs/require.min.js"></script>
<script>
//<![CDATA[
M.util.js_pending("core/first");
require(['core/first'], function() {
require(['core/prefetch'])
;
require.config({"paths":{"tableExport":"https:\/\/edu.stankin.ru\/local\/opentechnology\/js\/tableexport.jquery.plugin\/tableExport.min","bootstrap-table":"https:\/\/edu.stankin.ru\/local\/opentechnology\/js\/bootstrap-table\/bootstrap-table.min","bootstrap-table-locale-all":"https:\/\/edu.stankin.ru\/local\/opentechnology\/js\/bootstrap-table\/bootstrap-table-locale-all.min","bootstrap-table-toolbar":"https:\/\/edu.stankin.ru\/local\/opentechnology\/js\/bootstrap-table\/extensions\/toolbar\/bootstrap-table-toolbar.min","bootstrap-table-export":"https:\/\/edu.stankin.ru\/local\/opentechnology\/js\/bootstrap-table\/extensions\/export\/bootstrap-table-export.min"},"shim":{"bootstrap-table":{"deps":["jquery"],"exports":"$.fn.bootstrapTable"},"bootstrap-table-locale-all":{"deps":["bootstrap-table"],"exports":"$.fn.bootstrapTable.defaults"},"bootstrap-table-toolbar":{"deps":["bootstrap-table"],"exports":"$.fn.bootstrapTable.defaults"},"bootstrap-table-page-changed":{"deps":["bootstrap-table"],"exports":"$.fn.bootstrapTable.defaults"},"tableExport":{"deps":["jquery"],"exports":"$.fn.extend"},"bootstrap-table-export":{"deps":["bootstrap-table"],"exports":"$.fn.bootstrapTable.defaults"}}});
M.util.js_pending('atto_otiframe/otiframe'); require(['atto_otiframe/otiframe'], function(amd) {amd.init(); M.util.js_complete('atto_otiframe/otiframe');});;
M.util.js_pending('atto_otmagnifier/otmagnifier'); require(['atto_otmagnifier/otmagnifier'], function(amd) {amd.init(); M.util.js_complete('atto_otmagnifier/otmagnifier');});;
require(["media_videojs/loader"], function(loader) {
    loader.setUp('ru');
});;
M.util.js_pending('filter_otspoiler/atto_spoiler'); require(['filter_otspoiler/atto_spoiler'], function(amd) {amd.init(); M.util.js_complete('filter_otspoiler/atto_spoiler');});;
M.util.js_pending('theme_opentechnology/loader'); require(['theme_opentechnology/loader'], function(amd) {M.util.js_complete('theme_opentechnology/loader');});;
M.util.js_pending('theme_opentechnology/spellingmistake'); require(['theme_opentechnology/spellingmistake'], function(amd) {amd.init(); M.util.js_complete('theme_opentechnology/spellingmistake');});;
M.util.js_pending('theme_opentechnology/z-index-fixer'); require(['theme_opentechnology/z-index-fixer'], function(amd) {amd.fix("#h_rightblock_wrapper .popover-region,div#dock,#gridshadebox_content.absolute,div#gridshadebox_overlay"); M.util.js_complete('theme_opentechnology/z-index-fixer');});;
M.util.js_pending('theme_opentechnology/sticky'); require(['theme_opentechnology/sticky'], function(amd) {amd.init("#page-header .wrapper"); M.util.js_complete('theme_opentechnology/sticky');});;
M.util.js_pending('block_navigation/navblock'); require(['block_navigation/navblock'], function(amd) {amd.init("4"); M.util.js_complete('block_navigation/navblock');});;
M.util.js_pending('block_settings/settingsblock'); require(['block_settings/settingsblock'], function(amd) {amd.init("5", null); M.util.js_complete('block_settings/settingsblock');});;
M.util.js_pending('core_courseformat/courseeditor'); require(['core_courseformat/courseeditor'], function(amd) {amd.setViewFormat("11060", {"editing":false,"supportscomponents":true,"statekey":"1701486024_1701513824"}); M.util.js_complete('core_courseformat/courseeditor');});;

require(['core_courseformat/local/courseindex/placeholder'], function(component) {
    component.init('course-index-placeholder');
});
;

require(['core_courseformat/local/courseindex/drawer'], function(component) {
    component.init('courseindex');
});
;
M.util.js_pending('core_courseformat/local/content/activity_header'); require(['core_courseformat/local/content/activity_header'], function(amd) {amd.init(); M.util.js_complete('core_courseformat/local/content/activity_header');});;

require(['jquery', 'message_popup/notification_popover_controller'], function($, controller) {
    var container = $('#nav-notification-popover-container');
    var controller = new controller(container);
    controller.registerEventListeners();
    controller.registerListNavigationEventListeners();
});
;

require(
[
    'jquery',
    'core_message/message_popover'
],
function(
    $,
    Popover
) {
    var toggle = $('#message-drawer-toggle-656b0a6ba618e656b0a6ba1c2e60');
    Popover.init(toggle);
});
;
M.util.js_pending('theme_opentechnology/message_popup_render_navbar_output'); require(['theme_opentechnology/message_popup_render_navbar_output'], function(amd) {amd.init(); M.util.js_complete('theme_opentechnology/message_popup_render_navbar_output');});;
M.util.js_pending('local_opentechnology/otsupport-button'); require(['local_opentechnology/otsupport-button'], function(amd) {amd.init("ot-support-navbar-656b0a6ba6517", "mod\/assign\/view", 659204, 15); M.util.js_complete('local_opentechnology/otsupport-button');});;

    require(['core/moremenu'], function(moremenu) {
        moremenu(document.querySelector('#moremenu-656b0a6ba40c3-navbar-nav'));
    });
;

require(['theme_boost/drawers']);
;

require(['theme_boost/drawers']);
;

require(['theme_opentechnology/drawers'], function(drawers) {
    drawers.initHandleClickClose('theme_opentechnology-drawers-courseindex');
    drawers.adjustTogglerLeft('theme_opentechnology-drawers-courseindex');
    drawers.initAdjustDrawerHeight('theme_opentechnology-drawers-courseindex');
    drawers.changeTogglerOnToggle('theme_opentechnology-drawers-courseindex');
});
;

require(['theme_opentechnology/drawers'], function(drawers) {
    drawers.initHandleClickClose('theme_opentechnology-drawers-breadcrumbs');
    drawers.adjustTogglerLeft('theme_opentechnology-drawers-breadcrumbs');
    drawers.setDrawerRightToToggler('theme_opentechnology-drawers-breadcrumbs');
    drawers.changeTogglerOnToggle('theme_opentechnology-drawers-breadcrumbs');
});
;

        require(['jquery', 'core/custom_interaction_events'], function($, CustomEvents) {
            CustomEvents.define('#jump-to-activity', [CustomEvents.events.accessibleChange]);
            $('#jump-to-activity').on(CustomEvents.events.accessibleChange, function() {
                if (!$(this).val()) {
                    return false;
                }
                $('#url_select_f656b0a6ba1c2e61').submit();
            });
        });
    ;

require(['jquery', 'core_message/message_drawer'], function($, MessageDrawer) {
    var root = $('#message-drawer-656b0a6ba8eb3656b0a6ba1c2e62');
    MessageDrawer.init(root, '656b0a6ba8eb3656b0a6ba1c2e62', false);
});
;
M.util.js_pending('theme_opentechnology/dock'); require(['theme_opentechnology/dock'], function(amd) {amd.init("11060", "mod-assign-view", "incourse", "", 659204, "https:\/\/edu.stankin.ru\/theme\/image.php\/opentechnology\/theme_opentechnology\/1701486024\/dock_icon_04"); M.util.js_complete('theme_opentechnology/dock');});;
M.util.js_pending('local_opentechnology/otsupport-button'); require(['local_opentechnology/otsupport-button'], function(amd) {amd.init("ot-support-footer-656b0a6baeda7", "mod\/assign\/view", 659204, 15); M.util.js_complete('local_opentechnology/otsupport-button');});;

require(['theme_opentechnology/footer-popover'], function(FooterPopover) {
    FooterPopover.init();
});
;

M.util.js_pending('theme_boost/loader');
require(['theme_boost/loader'], function() {
    M.util.js_complete('theme_boost/loader');
});
;
M.util.js_pending('local_opentechnology/pendingevents'); require(['local_opentechnology/pendingevents'], function(amd) {amd.init(); M.util.js_complete('local_opentechnology/pendingevents');});;
M.util.js_pending('core/notification'); require(['core/notification'], function(amd) {amd.init(659204, []); M.util.js_complete('core/notification');});;
M.util.js_pending('core/log'); require(['core/log'], function(amd) {amd.setConfig({"level":"warn"}); M.util.js_complete('core/log');});;
M.util.js_pending('core/page_global'); require(['core/page_global'], function(amd) {amd.init(); M.util.js_complete('core/page_global');});;
M.util.js_pending('core/utility'); require(['core/utility'], function(amd) {M.util.js_complete('core/utility');});
    M.util.js_complete("core/first");
});
//]]>
</script>
<script src="https://edu.stankin.ru/theme/javascript.php/opentechnology/1701486024/footer"></script>
<script>
//<![CDATA[
M.str = {"moodle":{"lastmodified":"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0435 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435","name":"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435","error":"\u041e\u0448\u0438\u0431\u043a\u0430","info":"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f","yes":"\u0414\u0430","no":"\u041d\u0435\u0442","ok":"OK","viewallcourses":"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0432\u0441\u0435 \u043a\u0443\u0440\u0441\u044b","cancel":"\u041e\u0442\u043c\u0435\u043d\u0430","confirm":"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c","areyousure":"\u0412\u044b \u0443\u0432\u0435\u0440\u0435\u043d\u044b?","closebuttontitle":"\u0417\u0430\u043a\u0440\u044b\u0442\u044c","unknownerror":"\u041d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u043d\u0430\u044f \u043e\u0448\u0438\u0431\u043a\u0430","file":"\u0424\u0430\u0439\u043b","url":"URL","collapseall":"\u0421\u0432\u0435\u0440\u043d\u0443\u0442\u044c \u0432\u0441\u0451","expandall":"\u0420\u0430\u0437\u0432\u0435\u0440\u043d\u0443\u0442\u044c \u0432\u0441\u0451"},"repository":{"type":"\u0422\u0438\u043f","size":"\u0420\u0430\u0437\u043c\u0435\u0440","invalidjson":"\u041d\u0435\u0432\u0435\u0440\u043d\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430 JSON","nofilesattached":"\u041d\u0435 \u043f\u0440\u0438\u043a\u0440\u0435\u043f\u043b\u0435\u043d \u043d\u0438 \u043e\u0434\u0438\u043d \u0444\u0430\u0439\u043b","filepicker":"\u0412\u044b\u0431\u043e\u0440 \u0444\u0430\u0439\u043b\u0430","logout":"\u0412\u044b\u0445\u043e\u0434","nofilesavailable":"\u041d\u0435\u0442 \u043d\u0438 \u043e\u0434\u043d\u043e\u0433\u043e \u0444\u0430\u0439\u043b\u0430","norepositoriesavailable":"\u041a \u0441\u043e\u0436\u0430\u043b\u0435\u043d\u0438\u044e, \u043d\u0438 \u043e\u0434\u043d\u043e \u0438\u0437 \u0412\u0430\u0448\u0438\u0445 \u0442\u0435\u043a\u0443\u0449\u0438\u0445 \u0445\u0440\u0430\u043d\u0438\u043b\u0438\u0449 \u0444\u0430\u0439\u043b\u043e\u0432 \u043d\u0435 \u043c\u043e\u0436\u0435\u0442 \u0432\u0435\u0440\u043d\u0443\u0442\u044c \u0444\u0430\u0439\u043b\u044b \u0432 \u0437\u0430\u043f\u0440\u0430\u0448\u0438\u0432\u0430\u0435\u043c\u043e\u043c \u0444\u043e\u0440\u043c\u0430\u0442\u0435.","fileexistsdialogheader":"\u0424\u0430\u0439\u043b \u0441\u043e\u0437\u0434\u0430\u043d","fileexistsdialog_editor":"\u0424\u0430\u0439\u043b \u0441 \u044d\u0442\u0438\u043c \u0438\u043c\u0435\u043d\u0435\u043c \u0443\u0436\u0435 \u0431\u044b\u043b \u043f\u0440\u0438\u043a\u0440\u0435\u043f\u043b\u0435\u043d \u043a \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u0443\u0435\u043c\u043e\u043c\u0443 \u0442\u0435\u043a\u0441\u0442\u0443","fileexistsdialog_filemanager":"\u0424\u0430\u0439\u043b \u0441 \u044d\u0442\u0438\u043c \u0438\u043c\u0435\u043d\u0435\u043c \u0443\u0436\u0435 \u0431\u044b\u043b \u043f\u0440\u0438\u043a\u0440\u0435\u043f\u043b\u0435\u043d","renameto":"\u041f\u0435\u0440\u0435\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u0442\u044c \u0432 \u00ab{$a}\u00bb","referencesexist":"\u041d\u0430 \u044d\u0442\u043e\u0442 \u0444\u0430\u0439\u043b \u0435\u0441\u0442\u044c \u0441\u0441\u044b\u043b\u043a\u0438: {$a}","select":"\u0412\u044b\u0431\u0440\u0430\u0442\u044c"},"admin":{"confirmdeletecomments":"\u0412\u044b \u0443\u0432\u0435\u0440\u0435\u043d\u044b \u0432 \u0442\u043e\u043c, \u0447\u0442\u043e \u0441\u043e\u0431\u0438\u0440\u0430\u0435\u0442\u0435\u0441\u044c \u0443\u0434\u0430\u043b\u0438\u0442\u044c \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438?","confirmation":"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u0435"},"debug":{"debuginfo":"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e\u0431 \u043e\u0442\u043b\u0430\u0434\u043a\u0435","line":"\u0421\u0442\u0440\u043e\u043a\u0430","stacktrace":"\u0422\u0440\u0430\u0441\u0441\u0438\u0440\u043e\u0432\u043a\u0438 \u0441\u0442\u0435\u043a\u0430"},"langconfig":{"labelsep":":"}};
//]]>
</script>
<script>
//<![CDATA[
(function() {Y.use("moodle-filter_glossary-autolinker",function() {M.filter_glossary.init_filter_autolinking({"courseid":0});
});
Y.use("moodle-filter_mathjaxloader-loader",function() {M.filter_mathjaxloader.configure({"mathjaxconfig":"\nMathJax.Hub.Config({\n    config: [\"Accessible.js\", \"Safe.js\"],\n    errorSettings: { message: [\"!\"] },\n    skipStartupTypeset: true,\n    messageStyle: \"none\"\n});\n","lang":"ru"});
});
Y.on('domready', function() { Y.use("moodle-theme_opentechnology-blocks",function() {M.theme_ot.blocks.init();
}); });
M.util.help_popups.setup(Y);
 M.util.js_pending('random656b0a6ba1c2e65'); Y.on('domready', function() { M.util.js_complete("init");  M.util.js_complete('random656b0a6ba1c2e65'); });
})();
//]]>
</script>

</div>
<noscript class="secure_nojs">В вашем браузере отключен JavaScript</noscript>
</body>
</html>
'''

# Регулярное выражение
regex_pattern = r'(?:href|src)=["\']([^"\']+(\.(html|css|js|doc|docx|gif|jpg|png|pdf|xml|hml|jsx|tsx|asm|php|py|zip|7z|7zip)))["\']'
regex_pattern2 = r'(?:href|src)=["\']([^"\']+(.))["\']'

matches = re.findall(regex_pattern, html2_code)

# Вывод найденных соответствий
for match in matches:
    print(match[0])  # Выводим только первую группу захвата (URL)
