if (typeof jg === 'undefined') { jg = {'events': {}}; }
(function(doc) {
    var xhttp = new XMLHttpRequest();
    jg.request = function(req_args) {
        if (!req_args.context) { req_args.context = {}; }
        if (!req_args.success) { req_args.success = function() {}; }
        if (!req_args.failure) { req_args.failure = function() {}; }
        req_args.success.this = req_args.context;
        req_args.failure.this = req_args.context;

        xhttp.onreadystatechange = function() {
            if (xhttp.readyState == 4) {
                if (xhttp.status == 200) { req_args.success(xhttp.responseText); }
                else { req_args.failure(xhttp.status); }
                xhttp.onreadystatechange = null;
            }
        }

        req_args.method = req_args.method ? req_args.method : 'GET';
        xhttp.open(req_args.method, req_args.url, true);
        if (req_args.method === 'POST') { 
            xhttp.send(req_args.post_args);
        } else { xhttp.send(); }
    }

    jg.dispatch = function(e) {
        var data_evt = e.target.getAttribute('data-evt');
        var data_p = e.target.getAttribute('data-param');
        if (jg.events[data_evt]) { jg.events[data_evt](data_p); }
    };
    window.addEventListener('click', jg.dispatch);
}(document));
