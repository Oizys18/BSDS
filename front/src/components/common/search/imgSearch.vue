<template>
  <div class="search-container">
    <button class="search-button">
      <span class="material-icons"> search </span>
    </button>
    <input class="search-input" :placeholder="inputText" />
    <span class="bumper"></span>
  </div>
</template>

<script>
export default {
  name: "searchBar",
  props: {
    inputText: {
      type: String,
      required: true,
      default: "No input",
    },
  },
  methods: {
    imgSearch() {
      this.searched = true;
      let formData = new FormData();
      let url = "http://4756fe7c.ngrok.io";
      formData.append("image", this.file);
      axios
        .post(url + "/found/search/image/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((res) => {
          this.items = res.data.documents;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped>
.search-container {
  height: 100%;
  border: 1px solid black;
  padding: 0px 0px 0px 15px;
  border-radius: 20px;
  justify-content: space-around;
  align-items: center;
  display: flex;
}
.search-input {
  border: none;
  width: 70%;
  height: 70%;
  font-size: 2rem;
}
.bumper {
  width: 10%;
  height: 100%;
  border: none;
}
.search-button {
  border: none;
  display: flex;
  justify-content: flex-start;
  background: none;
  position: relative;
}
.material-icons {
  font-size: 50px;
}
</style>
