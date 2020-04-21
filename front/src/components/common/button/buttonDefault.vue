<template>
  <div class="button-default">{{ this.text }}</div>
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
}
.button-default:hover {
  background-color: grey;
}
</style>
