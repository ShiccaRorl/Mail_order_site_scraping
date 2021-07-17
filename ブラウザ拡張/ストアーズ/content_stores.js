
var sspage = new XMLSerializer().serializeToString(document);
var blob = new Blob([sspage], { "type" : "text/plain" });
var url = window.URL;
var bloburl = url.createObjectURL(blob);

// 新たにaタグを作成してダウンロード
var a = document.createElement('a');
a.download = 'stores.html';
a.href = bloburl;
a.click();

