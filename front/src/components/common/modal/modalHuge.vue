<template>
  <div class="modal-huge-container">
    <button v-on:click="exitModal">
      <div class="modal-huge-collide">✖</div>
    </button>
    <div class="modal-huge-title">title</div>
    <div class="modal-huge-content">text</div>
  </div>
</template>

<script>
export default {
  name: "modalHuge",
  data() {
    return {
      isClicked: false,
    };
  },
  methods: {
    exitModal() {
      this.isClicked = true;
      this.$emit("exit_Clicked", this.isClicked);
    },
  },
};
</script>

<style scoped>
.modal-huge-container {
  position: fixed;
  border: 1px solid black;
  border-radius: 15px;
  top: 20%;
  left: 35%;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 500px;
  height: 500px;
  background-color: white;
  color: black;
  font-size: 1rem;
}
</style>
