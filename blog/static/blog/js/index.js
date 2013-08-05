(function(doc) {
    jg.events['blogs_npage'] = blogs_npage;
    function failure(status) {
        alert("HTTPError: "+status);
    }

    function blogs_render(content) {
        var page_box = doc.getElementById('idx-page-box');
        page_box.parentNode.removeChild(page_box);
        doc.getElementById('left_body').innerHTML += content;
    }

    function blogs_npage(page) {
        var url = '/blog/page/'+page;
        var req = {
            'url': url,
            'success': blogs_render,
            'failure': failure
        };
        jg.request(req);
    }
}(document));
