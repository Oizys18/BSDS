<template>
  <div id="style-container">
    <div id="style-wrapper">
      <h5>Buttons</h5>
      buttonMicro
      <buttonMicro />
      buttonDefault
      <buttonDefault />
      buttonHuge
      <buttonHuge />
    </div>
    <div id="style-wrapper">
      <h5>dropdowns</h5>
      selectOne
      <selectOne />
    </div>
    <div id="style-wrapper">
      <h5>search</h5>
      searchBar
      <searchBar />
    </div>
    <div id="style-wrapper">
      <h5>card</h5>
      cardBig
      <div class="card-wrapper">
        <cardBig />
        <cardBig />
      </div>
    </div>
  </div>
</template>

<script>
import buttonDefault from "@/components/common/button/buttonDefault.vue";
import buttonHuge from "@/components/common/button/buttonHuge.vue";
import buttonMicro from "@/components/common/button/buttonMicro.vue";
import selectOne from "@/components/common/dropdown/selectOne.vue";
import searchBar from "@/components/common/search/searchBar.vue";
import cardBig from "@/components/common/card/cardBig.vue";
// import cardSmall from "@/components/common/card/cardSmall.vue";

export default {
  name: "componentTest",
  components: {
    buttonMicro,
    buttonDefault,
    buttonHuge,
    selectOne,
    searchBar,
    cardBig,
  },
};
</script>

<style scoped>
@import "../assets/css/global.css";
#style-container {
  display: flex;
  align-items: center;
  flex-direction: column;
}
#style-wrapper {
  padding: 10px;
  width: 50%;
  border: 1px solid black;
  border-style: dotted;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 5px 30px 30px 30px;
  margin: 10px;
}

.card-big-container {
  background-color: lightgrey;
}
</style>
