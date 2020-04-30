<template>
  <div>
    <div class="collider" v-on:click="exitModal"></div>
    <div class="modal-huge-wrapper">
      <div class="modal-huge-container">
        <button class="modal-huge-collide">
          <span v-on:click="exitModal">✖</span>
        </button>
        <div class="modal-huge-image">image</div>
        <div class="modal-huge-title">title</div>
        <div class="modal-huge-content">text</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "modalHuge",
  data() {
    return {};
  },
  props: {
    item: {
      type: Object,
      required: true,
    },
  },
  methods: {
    exitModal() {
      this.$store.state.showModal = false;
    },
  },
};
</script>

<style scoped>
.collider {
  position:absolute;
  width: 100vw;
  height: 100vh;
  z-index: 0;
  top:0;
  left:0;
  background:transparent;
}
.modal-huge-wrapper {
  /* position */
  position: fixed;
  top: 15%;
  left: 20%;
  /* modal shape */
  height: 70%;
  width: 60%;
  border: 1px solid black;
  border-radius: 15px;

  /* content */
  background-color: ghostwhite;
  color: black;
  font-size: 1rem;
}

.modal-huge-container {
  z-index: 10;
  width: 100%;
  height: 100%;
  display: grid;
  grid-template-rows: repeat(2, 50%);
  grid-template-columns: repeat(2, 50%);
}
.modal-huge-collide {
  position: absolute;
  right: 0;
  border: none;
  background: transparent;
  font-size: 25px;
}
.modal-huge-image {
  width: 100%;
  height: 100%;
  background: teal;
  border-radius: 15px;
  grid-row: 1 / 4;
}
.modal-huge-title {
  grid-row: 1/1;
  grid-column: 2/2;
  background: lightgreen;
  border-radius: 15px;
}
.modal-huge-content {
  grid-row: 2/2;
  grid-column: 2/2;
  background: yellow;
  border-radius: 15px;
}
</style>
