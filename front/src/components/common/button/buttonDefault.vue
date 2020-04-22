<template>
  <div class="button-default-container">
    <div
      class="button-default"
      :style="{ backgroundColor: bgColor, color: txtColor }"
    >
      {{ this.text }}
    </div>
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
  border: 1px solid black;
  border-radius: 6px;
  min-width: 3rem;
  margin: 3px;
  padding: 4px 8px 4px 8px;
  justify-content: center;
  display: inline-block;
  font-size: 15px;
  background-color: white;
  box-shadow: 2px 2px 5px 0 grey;
}
.button-default-container:hover {
  border-radius: 6px;
  box-shadow: 3px 3px 5px 0 grey;
}
.button-default-container:active {
  border-radius: 6px;
  box-shadow: 2px 2px 5px 0 grey;
}

</style>
