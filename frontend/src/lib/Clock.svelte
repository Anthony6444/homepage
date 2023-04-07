<script>
    let hours, minutes, seconds, date, ampm, day, dayofweek, month, year;

    let daysOfWeek = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ];
    let monthsOfYear = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ];

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
    $: day = date.getDate();
    $: dayofweek = daysOfWeek[date.getDay()];
    $: month = monthsOfYear[date.getMonth()];
    $: year = date.getFullYear();
</script>

<div class="date-time">
    <div class="clock">
        <span class="hr">{hours}:</span>
        <span class="min">{minutes}</span>
        <div class="vertalign">
            <span class="ampm">{ampm}</span>
            <span class="sec">{seconds}</span>
        </div>
    </div>
    <div class="date">
        <span class="day-of-week">{dayofweek},</span>
        <span class="month">{month}</span>
        <span class="day">{day},</span>
        <span class="year">{year}</span>
    </div>
</div>

<style>
    @import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap");

    .date {
        display: flex;
        font-size: 1.2em;
    }
    .date span { 
        padding-left: 0.3em;
    }
    .date-time {
        float: right;
        font-family: "Poppins", sans-serif;
        flex-direction: column;
        display: flex;
        margin: 2em 5em 0 0;
    }
    .hr,
    .min {
        font-size: 6em;
    }
    .min {
        color: cadetblue;
    }
    .clock {
        display: flex;
        flex-direction: row;
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
