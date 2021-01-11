CKEDITOR.editorConfig = function (config) {

	config.removePlugins = 'image';
	config.extraPlugins = 'image2';
    config.extraPlugins = 'uploadimage';
	config.filebrowserUploadUrl = '/upload/';
    config.imageUploadUrl = '/upload/';

	config.toolbarGroups = [
		{ name: 'document', groups: [ 'mode', 'document', 'doctools' ] },
		{ name: 'clipboard', groups: [ 'clipboard', 'undo' ] },
		{ name: 'editing', groups: [ 'find', 'selection', 'spellchecker', 'editing' ] },
		{ name: 'forms', groups: [ 'forms' ] },
		{ name: 'basicstyles', groups: [ 'basicstyles', 'cleanup' ] },
		{ name: 'paragraph', groups: [ 'list', 'indent', 'blocks', 'align', 'bidi', 'paragraph' ] },
		{ name: 'links', groups: [ 'links' ] },
		{ name: 'insert', groups: [ 'insert' ] },
		{ name: 'styles', groups: [ 'styles' ] },
		{ name: 'colors', groups: [ 'colors' ] },
		{ name: 'tools', groups: [ 'tools' ] },
		{ name: 'others', groups: [ 'others' ] },
		{ name: 'about', groups: [ 'about' ] }
	];
	config.removeButtons = 'Anchor,Subscript,Superscript,Strike,Iframe';

    config.wordcount = {
        showParagraphs: true,
        showWordCount: false,
        showCharCount: true,
        countSpacesAsChars: false,
        countHTML: false,
        countLineBreaks: false,
    };

    config.width = '100%';
    config.height = '30em';

};