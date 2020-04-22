<template>
  <div id="lost-wrapper">
      <cardBig/>
      <cardBig/>
  </div>
</template>

<script>
import cardBig from "@/components/common/card/cardBig.vue";
export default {
  name: "foundList",
  components:{
      cardBig
  }
};
</script>

<style>
#lost-wrapper {
  width: 100%;
  height: 100%;
  margin-top: 150px;
  justify-content: center;
  align-items: center;
  display: flex;
}
</style>
