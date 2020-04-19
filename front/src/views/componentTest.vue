<template>
  <div id="style-container">
    <div id="style-wrapper">
        <h5>Buttons</h5>
      <buttonMicro />
      <buttonDefault />
      <buttonHuge />
    </div>
    <div id="style-wrapper">
        <h5>dropdowns</h5>
        <selectOne/>
    </div>
  </div>
</template>

<script>
import buttonDefault from "@/components/common/button/buttonDefault.vue";
import buttonHuge from "@/components/common/button/buttonHuge.vue";
import buttonMicro from "@/components/common/button/buttonMicro.vue";
import selectOne from "@/components/common/dropdown/selectOne.vue";
export default {
  name: "componentTest",
  components: { 
    buttonMicro,
    buttonDefault,
    buttonHuge,
    selectOne,
  },
};
</script>

<style scoped>
#style-container{
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}
#style-wrapper{
    border:1px solid black;
    border-style: dotted;
    display: inline-block;
    justify-content: center;
    padding:5px 30px 30px 30px;
    margin:10px;
}

</style>
