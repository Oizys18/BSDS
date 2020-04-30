<template>
  <div class="pnf-wrapper">
    <div class="pnf">
      PNF
    </div>
    <div class="pnfnum">
      404
    </div>
  </div>
</template>

<script>
export default {
  name: "pnf",
};
</script>

<style scoped>
.pnf-wrapper {
  justify-content: center;
  align-items: center;
  display: flex;
}
.pnf {
  top: 15%;
  left: 25%;
  position: fixed;
  font-size: 20rem;
  font-weight: bolder;
  color: #38618c;
  text-shadow: 20px 20px 5px rgb(105, 105, 105);
}
.pnfnum {
  top: 38%;
  position: fixed;
  left: 35%;
  font-size: 23rem;
  font-weight: bolder;
  color: #0a95ff;
  text-shadow: 20px 20px 5px rgb(105, 105, 105);
}
</style>
