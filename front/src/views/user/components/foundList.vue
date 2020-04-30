<template>
  <div id="found-wrapper">
    <navbar />
    <div id="found-card-container">
      <div
        @click="showModal(item)"
        v-for="(item, index) in items"
        :key="index.id"
        class="found-card"
      >
        <cardSmall :item="item" />
      </div>
    </div>
    <div v-if="this.$store.state.showModal" class="user-index-modal">
      <modalHuge :item="this.item" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import navbar from "@/views/user/components/navbar";
import cardSmall from "@/components/common/card/cardSmall.vue";
import modalHuge from "@/components/common/modal/modalHuge.vue";
export default {
  name: "foundList",
  components: {
    navbar,
    modalHuge,
    cardSmall,
  },
  data() {
    return {
      item: Object,
      items: Object,
      isClicked: false,
      pageSize: 8,
      imagesrc: `media/no_image.png`,
      baseurl: process.env.VUE_APP_BASE_URL,
    };
  },
  methods: {
    showModal(item) {
      this.$store.state.showModal = true;
      this.item = item;
    },
  },
  mounted() {
    this.$store.state.loading = true;
    console.log(this.baseurl + "found/search/");
    axios
      .get(this.baseurl + "found/search/")
      .then((res) => {
        this.$store.state.loading = false;
        this.items = res.data.documents.slice(0, 9);
        console.log(this.items[0]);
      })
      .catch((err) => {
        console.log(err);
      });
    if (this.$store.state.documents) {
      this.items = this.$store.state.documents;
      this.$store.state.documents = {};
    }
  },
};
</script>

<style scoped>
#found-wrapper {
  height: 100%;
  margin-top: 18vh;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  display: flex;
  flex-wrap: wrap;
}
#found-card-container {
  display: grid;

  grid-template-rows: repeat(3, 230px);
  grid-template-columns: repeat(3, 230px);
  justify-content: space-around;
  align-items: center;
  margin: 10px;
}
.found-card {
  /* margin: auto; */
  display: flex;
  box-sizing: border-box;
}
</style>
