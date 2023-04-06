<script>
    let hours, minutes, seconds, date, ampm;

    setInterval(() => {
        date = new Date();
    }, 1000);
    $: date = new Date();
    $: hours = (
        date.getHours() < 12 ? date.getHours() : date.getHours() - 12
    ).toString();
    $: minutes = date.getMinutes().toString().padStart(2, "0");
    $: seconds = date.getSeconds().toString().padStart(2, "0");
    $: ampm = date.getHours() < 12 ? "AM" : "PM";
</script>

<div class="clock">
    <span class="hr">{hours}</span>
    <span class="bigsep">:</span>
    <span class="min">{minutes}</span>
    <div class="vertalign">
        <span class="ampm">{ampm}</span>
        <span class="sec">{seconds}</span>
    </div>
</div>

<style>
    @import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap");
    .clock {
        float: right;
        font-family: "Poppins", sans-serif;
        display: flex;
        margin: 2em 5em 0 0 ;
    }
    .hr,
    .bigsep,
    .min {
        font-size: 6em;
    }
    .min {
        color: cadetblue;
    }
    .clock .ampm {
        font-size: 2em;
    }
    .clock .sec {
        font-size: 2em;
    }
    .clock .vertalign {
        padding-top: 1.2em;
        padding-bottom: 1.4em;
        padding-left: 1em;
        display: flex;
        flex-direction: column;
        justify-content: space-evenly;
        align-items: center;
    }
</style>
