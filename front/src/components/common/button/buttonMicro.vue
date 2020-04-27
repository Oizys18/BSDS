<template>
  <div
    class="button-micro"
    :style="{ backgroundColor: bgColor, color: txtColor }"
  >
    {{ this.text }}
  </div>
</template>

<script>
export default {
  name: "buttonMicro",
  props: {
    text: {
      type: String,
      required: true,
      default: "micro",
    },
    bgColor: {
      type: String,
    },
    txtColor: {
      type: String,
    },
  },
};
</script>

<style scoped>
.button-micro {
  border: 1px solid #999999;
  min-width: 2rem;
  border-radius: 5px;
  margin: 3px;
  padding: 3px 6px 3px 6px;
  justify-content: center;
  display: inline-block;
  font-size: 10px;
  background-color: white;
}
.button-micro:hover {
  box-shadow: 2px 2px 10px 0 grey;
  border: 1px solid white;
  outline: none;
}
.button-micro:active {
  box-shadow: inset 0 0 5px grey;
  border: 1px solid grey;
  outline: none;
}
</style>
