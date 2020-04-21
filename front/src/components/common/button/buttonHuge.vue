<template>
  <div class="button-huge">{{ this.text }}</div>
</template>

<script>
export default {
  name: "bottonHuge",
  props: {
    text: {
      type: String,
      required: true,
      default: "huge",
    },
  },
};
</script>

<style scoped>
.button-huge {
  border: 1px solid black;
  border-radius: 8px;
  min-width: 5rem;
  margin: 3px;
  padding: 6px 12px 6px 12px;
  justify-content: center;
  display: inline-block;
  font-size: 25px;
}
.button-huge:hover {
  background-color: grey;
}
</style>
