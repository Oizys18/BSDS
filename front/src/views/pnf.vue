<template>
  <div class="pnf-back">
    <div class="pnf-wrapper">
      <div class="pnf" id="pnflogo">
        <img class="logo" @click="go('/')" src="@/assets/images/mainlogo.png" />
        <br />
        페이지가 없습니다!
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "pnf",
  methods: {
    mouseIsMoving(e) {
      console.log(e);
      var hamX = document.getElementById("pnflogo").offsetLeft;
      var hamY = document.getElementById("pnflogo").offsetTop;
      var x = (hamX - e.pageX) * 0.1;
      var y = (hamY - e.pageY) * 0.1;
      document.getElementById("pnflogo").style.webkitTransform =
        "translate(" + x + "px" + "," + y + "px)";
    },
  },
  mounted() {
    window.addEventListener("mousemove", this.mouseIsMoving);
  },
};
</script>

<style scoped>
.logo {
  width: 50%;
}
.pnf-wrapper {
  justify-content: center;
  align-items: center;
  display: flex;
}
.pnf {
  top: 25%;
  left: 25%;
  font-size: 4em;
  position: fixed;
  font-weight: bolder;
  color: rgb(240, 95, 95);
}
</style>
