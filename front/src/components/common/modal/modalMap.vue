<template>
  <div class="modal-map-wrapper">
    <div class="modal-map-container">
      <button class="modal-map-collide" v-on:click="exitModal">
        <span>✖</span>
      </button>
      <div class="mapapp-container">
        <div id="map" class="kakao-map search-map"></div>
      </div>
      <div class="modal-map-btn">
        <buttonHuge :text="btnText" :bgColor="bgColor" />
      </div>
    </div>
  </div>
</template>

<script>
import buttonHuge from "@/components/common/button/buttonHuge.vue";
export default {
  name: "modalMap",
  components:{
    buttonHuge
  },
  data() {
    return {
      address: "",
      addressList: [],
      isClicked: false,
      btnText:"여기에요!",
      bgColor:"white",
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
  top: 0;
  left: 0;
  position: relative;
  text-align: center;
}
.search-map {
  position: relative;
  width: 100%;
  height: 40vh;
  margin-bottom: 20px;
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

.modal-map-wrapper {
  /* position */
  position: fixed;
  top: 32%;
  left: 30%;

  /* modal shape */
  height: 50%;
  width: 40%;
  border: 1px solid black;
  /* border-radius: 15px; */

  /* content */
  background-color: ghostwhite;
  color: black;
  font-size: 1rem;
}

.modal-map-container {
  width: 100%;
  height: 100%;
}

.modal-map-collide {
  position: absolute;
  right: 0;
  border: none;
  background: transparent;
  font-size: 40px;
  z-index: 10;
}
</style>
