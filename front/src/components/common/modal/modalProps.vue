<template>
  <div class="modal-huge-wrapper">
    <div class="modal-huge-container">
      <button class="modal-huge-collide" v-on:click="exitModal">
        <span>✖</span>
      </button>
      <div class="modal-huge-image"></div>
      <div class="modal-huge-title">title</div>
      <div class="modal-huge-content">{{ data.content }}</div>
    </div>
  </div>
</template>

<script>
// import  from 'vuex'
export default {
  name: "modalHuge",
  data() {
    return {
      isClicked: false,
    };
  },
  props: {
    data: {
      type: Object,
      default: null
    }
  },
  methods: {
    exitModal() {
      this.isClicked = true;
      this.$emit("exit_Clicked", this.isClicked);
    },
  }
};
</script>

<style scoped>
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


  /* justify-content: center;
  align-items: center; */
}

.modal-huge-container{
  width:100%;
  height:100%;
    /* contents align */
  display: grid;
  grid-template-rows: repeat(2,50%);
  grid-template-columns: repeat(2, 50%);

}


.modal-huge-collide {
  position: absolute;
  right: 0;
  border:none;
  background:transparent;
  z-index:10;
  font-size:25px;
}
.modal-huge-image {
  width: 100%;
  height: 100%;
  background: teal;
  border-radius: 15px;
  grid-row: 1 / 4;
}
.modal-huge-title{
  grid-row:1/1;
  grid-column:2/2;
  background: lightgreen;
  border-radius: 15px;
}
.modal-huge-content{
  grid-row:2/2;
  grid-column: 2/2;
  background: yellow;
  border-radius: 15px;
}
</style>
