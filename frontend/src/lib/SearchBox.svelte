<script>
    import jQuery from "jquery";
    const jq = jQuery;
    jq(document).ready(function () {
        jq("#search").on("focus", function () {
            jq(".search-box").addClass("border-searching");
            jq(".search-icon").addClass("si-rotate");
        });
        jq("#search").on("blur", function () {
            jq(".search-box").removeClass("border-searching");
            jq(".search-icon").removeClass("si-rotate");
        });
        jq("#search").on("keyup", function () {
            if (jq(this).val().toString().length > 0) {
                jq(".go-icon").addClass("go-in");
            } else {
                jq(".go-icon").removeClass("go-in");
            }
        });
        jq(".go-icon").on("click", function () {
            jq(".search-form").trigger("submit");
        });
    });

    export let searchEngineName;
</script>

<div class="container">
    <h1>{searchEngineName}</h1>
    <div class="search-box">
        <div class="search-icon"><i class="fa fa-search search-icon" /></div>
        <form action="/api/search" method="GET" class="search-form">
            <input
                type="text"
                placeholder="Search"
                id="search"
                name="q"
                autocomplete="off"
            />
            <input type="hidden" id="uuid" name="uuid" />
        </form>
        <svg
            class="search-border"
            version="1.1"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            x="0px"
            y="0px"
            viewBox="0 0 671 111"
            style="enable-background:new 0 0 671 111;"
            xml:space="preserve"
        >
            <path
                class="border"
                d="M335.5,108.5h-280c-29.3,0-53-23.7-53-53v0c0-29.3,23.7-53,53-53h280"
            />
            <path
                class="border"
                d="M335.5,108.5h280c29.3,0,53-23.7,53-53v0c0-29.3-23.7-53-53-53h-280"
            />
        </svg>
        <div class="go-icon"><i class="fa fa-arrow-right" /></div>
    </div>
</div>
