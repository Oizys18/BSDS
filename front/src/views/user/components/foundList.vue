<template>
  <div id="found-wrapper" :key="foundKey">
    <navbar />
    <div id="found-card-container">
      <div
        @click="showModal(item)"
        v-for="(item, index) in items"
        :key="index.id"
        class="found-card"
      >
        <cardSmall :item="item" class="animated delay-0.1s zoomIn faster" />
      </div>
    </div>
    <div v-if="this.$store.state.showModal" class="user-index-modal">
      <modalProps :data="this.item" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import navbar from "@/views/user/components/navbar";
import cardSmall from "@/components/common/card/cardSmall.vue";
import modalProps from "@/components/common/modal/modalProps.vue";
export default {
  name: "foundList",
  components: {
    navbar,
    modalProps,
    cardSmall,
  },
  data() {
    return {
      item: Object,
      items: Object,
      foundKey: 0,
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
  watch: {
    $route() {
      this.$store.state.showModal = false;
    },
    items() {
      this.foundKey += 1;
    },
  },
  mounted() {
    this.$store.state.loading = true;
    if (this.$store.state.documents[0]) {
      this.$store.state.loading = false;
      this.items = this.$store.state.documents;
      this.$store.state.documents = {};
    } else {
      this.$store.state.loading = false;
      axios
        .get(this.baseurl + "found/search/")
        .then((res) => {
          this.items = res.data.documents.slice(0, 9);
        })
        .catch((err) => {
          console.log(err);
        });
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
  justify-content: center;
  align-items: center;
  margin: 10px;
}
.found-card {
  display: flex;
  justify-content: center;
  box-sizing: border-box;
}
</style>
