<template>
  <div class="button-micro">{{ this.text }}</div>
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
  },
};
</script>

<style scoped>
.button-micro {
  border: 1px solid black;
  min-width: 2rem;
  border-radius: 5px;
  margin: 3px;
  padding: 3px 6px 3px 6px;
  justify-content: center;
  display: inline-block;
  font-size: 10px;
}
.button-micro:hover {
  background-color: grey;
}
</style>
