<script>
    import Clock from "./lib/Clock.svelte";
  let searchEngineName = "Name of Search Engine";
  import SearchBox from "./lib/SearchBox.svelte";
</script>

<main>
  <Clock/>
  <SearchBox {searchEngineName}/>
</main>
