(function(doc) {
    jg.events['blogs_npage'] = blogs_npage;
    jg.events['toggle_year'] = toggle_year;
    jg.events['month_select'] = month_select;

    function failure(status) {
        alert("HTTPError: "+status);
    }

    function blogs_render(content) {
        var page_box = doc.getElementById('idx-page-box');
        page_box.parentNode.removeChild(page_box);
        doc.getElementById('left_body').innerHTML += content;
    }

    function month_select(args) {
        var m = args.month;
        var y = args.year;
        window.location = '/blog/'+y+'/'+m;
    }

    function blogs_npage(args) {
        var url = '/blog/page/'+args.page;
        var req = {
            'url': url,
            'success': blogs_render,
            'failure': failure
        };
        jg.request(req);
    }

    function toggle_year(args) {
        var div = doc.getElementById('archive-'+args.year);
        var div_height = div.style.height;
        var collapsed = (!div_height || div_height === '0px') 
        if (collapsed) { div.style.height = '25px'; }
        else { div.style.height = '0px'; }
    }
}(document));
