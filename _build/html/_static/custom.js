document.addEventListener("DOMContentLoaded", function() {
    (function() { var method; var noop = function() {}; var methods = ['assert', 'clear', 'count', 'debug', 'dir', 'dirxml', 'error', 'exception', 'group', 'groupCollapsed', 'groupEnd', 'info', 'log', 'markTimeline', 'profile', 'profileEnd', 'table', 'time', 'timeEnd', 'timeline', 'timelineEnd', 'timeStamp', 'trace', 'warn']; var length = methods.length; var console = (window.console = window.console || {}); while (length--) { method = methods[length]; if (!console[method]) { console[method] = noop; } } }());
    feather.replace();
    var $window = $(window),
        $head = $('head'),
        $body = $('body'),
        $sidebar = $('#site-navigation'),
        $sidebarToggle = $('navbar-toggler');

    function setContrast() { var setContrast = localStorage.setContrast; if (setContrast == 1) { $body.addClass('dark-theme');
            $('.btn__contrast').addClass('btn-active'); } }
    setContrast();
    $('.btn__contrast').on('click', function(event) { event.preventDefault();
        event.stopPropagation(); if ($(this).hasClass('btn-active')) { $(this).removeClass('btn-active');
            localStorage.setContrast = 0;
            $body.removeClass('dark-theme'); } else { $(this).addClass('btn-active');
            localStorage.setContrast = 1;
            $body.addClass('dark-theme'); } });

    function setSidebar() { var setSidebar = localStorage.setSidebar; if ((setSidebar == 1) && ($sidebar.hasClass('persistent')) && ($(window).width() > 1340)) { openSidebar(); } }
    setSidebar();

    function openSidebar() { $sidebarToggle.addClass('btn-active');
        $sidebar.removeClass('inactive');
        $(".qe-toolbar svg.feather.feather-menu").replaceWith(feather.icons.x.toSvg());
        localStorage.setSidebar = 1; }

    function closeSidebar() { $sidebarToggle.removeClass('btn-active');
        $sidebar.addClass('inactive');
        $(".qe-toolbar svg.feather.feather-x").replaceWith(feather.icons.menu.toSvg());
        localStorage.setSidebar = 0; }

    $(document).on('click', '.btn__sidebar', function(event) {
        event.preventDefault();
        event.stopPropagation();
        if ($sidebar.hasClass('inactive')) { openSidebar(); } else { closeSidebar(); }
        if (window.innerWidth <= 1340) { $(document.body).on('click', function(e) { if (!$(event.target).is('.sidebar *')) { closeSidebar();
                    $body.off('click'); } }); }
    });
    $('.btn__top').on('click', function(event) { event.preventDefault();
        event.stopPropagation();
        $('html, body').animate({ scrollTop: 0 }, 'slow'); });

    $('.btn__fullscreen').on('click', function() { event.preventDefault();
        event.stopPropagation();
        $(this).toggleClass('btn-active'); if (document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement || document.msFullscreenElement) { if (document.exitFullscreen) { document.exitFullscreen(); } else if (document.msExitFullscreen) { document.msExitFullscreen(); } else if (document.mozCancelFullScreen) { document.mozCancelFullScreen(); } else if (document.webkitExitFullscreen) { document.webkitExitFullscreen(); } } else { if (document.documentElement.requestFullscreen) { document.documentElement.requestFullscreen(); } else if (document.documentElement.webkitRequestFullscreen) { document.documentElement.webkitRequestFullscreen(); } else if (document.documentElement.mozRequestFullScreen) { document.documentElement.mozRequestFullScreen(); } else if (document.documentElement.msRequestFullscreen) { document.documentElement.msRequestFullscreen(); } } });

    function setFontSize() { var toolbarFont = localStorage.toolbarFont; if (toolbarFont == 1) { $('html').addClass('font-plus'); } else if (toolbarFont == -1) { $('html').addClass('font-minus'); } else { $('html').removeClass('font-plus');
            $('html').removeClass('font-minus');
            localStorage.toolbarFont = 0; } }
    setFontSize();
    $('.btn__plus').on('click', function(event) {
        event.preventDefault();
        event.stopPropagation();
        var toolbarFont = parseInt(localStorage.getItem('toolbarFont')) + 1;
        if (toolbarFont > 0) { toolbarFont = 1; }
        localStorage.toolbarFont = toolbarFont;
        setFontSize();
    });
    $('.btn__minus').on('click', function(event) {
        event.preventDefault();
        event.stopPropagation();
        var toolbarFont = parseInt(localStorage.getItem('toolbarFont')) - 1;
        if (toolbarFont < 0) { toolbarFont = -1; }
        localStorage.toolbarFont = toolbarFont;
        setFontSize();
    });
    const collapseAccToHeight = (el, elH) => {
        if (el.includes("tag_collapse")) {
            index = el.indexOf("-")
            height = el.substring(index + 1)
            if (height && !isNaN(height)) { elH.style.height = parseInt(height) + 0.5 + "em" }
        }
    }
    const collapsableCodeBlocks = document.querySelectorAll("div[class^='cell tag_collapse']");
    for (var i = 0; i < collapsableCodeBlocks.length; i++) {
        const collapsableCodeBlocksH = collapsableCodeBlocks[i].querySelectorAll(".highlight")[0]
        collapsableCodeBlocks[i].classList.forEach(el => { collapseAccToHeight(el, collapsableCodeBlocksH) })
        const toggleContainer = document.createElement('div');
        toggleContainer.innerHTML = '<a href="#" class="toggle toggle-less" style="display:none;"><span class="icon icon-angle-double-up"></span><em>Show less...</em></a><a href="#" class="toggle toggle-more"><span class="icon icon-angle-double-down"></span><em>Show more...</em></a>';
        collapsableCodeBlocksH.parentNode.insertBefore(toggleContainer, collapsableCodeBlocksH.nextSibling);
    }
    const collapsableCodeToggles = document.querySelectorAll("div[class^='cell tag_collapse'] .toggle");
    for (var i = 0; i < collapsableCodeToggles.length; i++) {
        collapsableCodeToggles[i].addEventListener('click', function(e) {
            e.preventDefault();
            var codeBlock = this.closest('div[class^="cell tag_collapse"]');
            codeBlockH = codeBlock.querySelector('.highlight')
            if (codeBlock.classList.contains('expanded')) { codeBlock.classList.remove('expanded');
                this.style.display = 'none';
                this.nextSibling.style.display = 'block';
                codeBlock.classList.forEach(el => { collapseAccToHeight(el, codeBlockH) }) } else { codeBlock.classList.add('expanded');
                this.style.display = 'none';
                this.previousSibling.style.display = 'block';
                codeBlockH.style.height = "auto" }
        });
    }
    const contentTables = document.querySelectorAll('.qe-page__content table');
    for (var i = 0; i < contentTables.length; i++) { var wrapper = document.createElement('div');
        wrapper.classList.add('table-container');
        contentTables[i].parentNode.insertBefore(wrapper, contentTables[i]);
        wrapper.appendChild(contentTables[i]); }
    if (document.getElementById('downloadButton')) { const template = document.getElementById('downloadPDFModal');
        template.style.display = 'block';
        tippy('#downloadButton', { content: template, theme: 'light-border', animation: 'shift-away', inertia: true, duration: [200, 200], arrow: true, arrowType: 'round', delay: [200, 200], interactive: true, trigger: "click" }); }
    if (document.getElementById('settingsButton')) { const template = document.getElementById('settingsModal');
        template.style.display = 'block';
        tippy('#settingsButton', { content: template, theme: 'light-border', animation: 'shift-away', inertia: true, duration: [200, 200], arrow: true, arrowType: 'round', delay: [200, 200], interactive: true, trigger: "click" }); }
    window.onChangeListener = () => {
        let private = document.getElementById("launcher-private-input").value
        if ($(this.event.currentTarget)[0].getAttribute("id").indexOf("private") > -1) {
            if (!private.includes("http") && !private.includes("https")) { private = "http://" + private }
            let pagename = document.getElementsByClassName("page")[0].getAttribute("id")
            let repo = document.getElementById("launcher-private-input").dataset.repourl
            let urlpath = document.getElementById("launcher-private-input").dataset.urlpath
            const repoPrefix = "/jupyter/hub/user-redirect/git-pull?repo=" + repo + "&urlpath=" + urlpath;
            url = private + repoPrefix + pagename + ".ipynb";
            launchButton.getElementsByTagName("a")[0].setAttribute("href", url)
        } else {
            let url = document.getElementById("launcher-public-input").value
            let launchButton = document.getElementById("launchButton")
            launchButton.getElementsByTagName("a")[0].setAttribute("href", url)
        }
    }
    tippy('[data-tippy-content]', { touch: false, });
});




    // $(document).click(function () {
    //     if(window.innerWidth <= 1340){
    //     if (document.getElementById("site-navigation").getAttribute("class") == 'col-12 col-md-3 bd-sidebar site-navigation show' || document.getElementById("site-navigation").getAttribute("class") == 'col-12 col-md-3 bd-sidebar site-navigation collapse show'){
    //         $("#navbar-toggler").trigger('click');
    //     }}
    // })

    $(document).click(function (e) {

         e = window.event || e; // 兼容IE7
        obj = $(e.srcElement || e.target);

        if(window.innerWidth <= 1340){

        if (!$(obj).is("#site-navigation *")) {

        if (document.getElementById("site-navigation").getAttribute("class") == 'col-12 col-md-3 bd-sidebar site-navigation show' || document.getElementById("site-navigation").getAttribute("class") == 'col-12 col-md-3 bd-sidebar site-navigation collapse show'){
            $("#navbar-toggler").trigger('click');}

        }
        }
    })