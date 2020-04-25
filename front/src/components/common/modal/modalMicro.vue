<template>
  <div class="modal-micro-wrapper">
    <div class="modal-micro-container">
      <button class="modal-micro-collide" v-on:click="exitModal">
        <span>✖</span>
      </button>
      <div class="modal-micro-image">image</div>
      <div class="modal-micro-title">title</div>
      <div class="modal-micro-content">text</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "modalMicro",
  data() {
    return {
      isClicked: false,
    };
  },
  props: {
    image: {
      type: String,
      default: "No Image",
    },
    title: {
      type: String,
      required: true,
      default: "No title",
    },
    text: {
      type: String,
      required: true,
      default: "No text",
    },
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
.modal-micro-wrapper {
  /* position */
  position: fixed;
  top: 30%;
  left: 30%;

  /* modal shape */
  height: 40%;
  width: 40%;
  border: 1px solid black;
  border-radius: 15px;

  /* content */
  background-color: ghostwhite;
  color: black;
  font-size: 1rem;
}

.modal-micro-container {
  width: 100%;
  height: 100%;

  /* contents align */
  display: grid;
  grid-template-rows: repeat(2, 50%);
  grid-template-columns: repeat(2, 50%);
}

.modal-micro-collide {
  position: absolute;
  right: 0;
  border: none;
  background: transparent;
  font-size: 25px;
}
.modal-micro-image {
  width: 100%;
  height: 100%;
  background: teal;
  border-radius: 15px;
  grid-row: 1 / 4;
}
.modal-micro-title {
  grid-row: 1/1;
  grid-column: 2/2;
  background: lightgreen;
  border-radius: 15px;
}
.modal-micro-content {
  grid-row: 2/2;
  grid-column: 2/2;
  background: yellow;
  border-radius: 15px;
}
</style>
