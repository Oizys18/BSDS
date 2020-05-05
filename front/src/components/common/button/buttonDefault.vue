<template>
  <div
    class="button-default"
    :style="{ backgroundColor: bgColor, color: txtColor }"
  >
    {{ this.text }}
  </div>
</template>

<script>
export default {
  name: "buttonDefault",
  props: {
    text: {
      type: String,
      required: true,
      default: "default",
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
.button-default {
  border: 1px solid #999999;
  border-radius: 6px;
  min-width: 3rem;
  margin: 3px;
  justify-content: center;
  display: inline-block;
  font-size: 15px;
  background-color: white;
  padding: 3px 6px 3px 6px;
}
.button-default:hover {
  box-shadow: 2px 2px 10px 0 grey;
  border: 1px solid white;
  outline: none;
}
.button-default:active {
  box-shadow: inset 0 0 5px grey;
  border: 1px solid grey;
  outline: none;
}
</style>
