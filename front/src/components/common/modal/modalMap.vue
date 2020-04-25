<template>
  <div class="modal-micro-wrapper">
    <div class="modal-micro-container">
      <button class="modal-micro-collide" v-on:click="exitModal">
        <span>✖</span>
      </button>
      <div class="mapapp-container">
        <label for="address-input" style="padding:3px; margin:10px;"
          >주소입력</label
        >
        <input
          type="text"
          id="address-input"
          v-model="address"
          @keydown.enter="getXY"
          style="border:1px solid; margin:10px; padding:10px;"
        />
        <div class="map-search-btn">검색</div>

        <div id="map" class="kakao-map search-map"></div>
        <br />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "modalMap",
  data() {
    return {
      address: "",
      addressList: [],
      isClicked: false,
    };
  },
  methods: {
    exitModal() {
      this.isClicked = true;
      this.$emit("exit_Clicked", this.isClicked);
    },
    initMap() {
      var container = document.getElementById("map");
      var options = {
        center: new kakao.maps.LatLng(33.450701, 126.570667),
        level: 3,
      };
      var map = new kakao.maps.Map(container, options); //마커추가하려면 객체를 아래와 같이 하나 만든다.
      var marker = new kakao.maps.Marker({ position: map.getCenter() });
      marker.setMap(map);
    },
    addScript() {
      const script = document.createElement("script");
      /* global kakao */
      script.onload = () => kakao.maps.load(this.initMap);
      script.src =
        "http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=69d0c2177d4e8cf1a0f7361daafcc7ac";
      document.head.appendChild(script);
    },
  },
  mounted() {
    window.kakao && window.kakao.maps ? this.initMap() : this.addScript();
  },
};
</script>
<style scoped>
.mapapp-container {
  position: relative;
  top: 50px;
  left: 0;
  text-align: center;
}
.search-map {
  position: relative;
  width: 300px;
  height: 300px;
}
.map-search-btn {
  display: inline-block;
  background-color: #fbedeb;
  border-radius: 20px;
  font-size: 1.3rem;
  padding: 0.4em 0.7em 0.4em 0.7em;
  cursor: pointer;
  font-weight: bold;
}

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
}

.modal-micro-collide {
  position: absolute;
  right: 0;
  border: none;
  background: transparent;
  font-size: 25px;
}
</style>
