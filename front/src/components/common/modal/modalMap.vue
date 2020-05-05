<template>
  <div class="modal-map-wrapper">
    <div class="modal-map-container">
      <div class="mapapp-container">
        <div id="map" class="kakao-map search-map"></div>
      </div>
    </div>
    <div class="confirm" v-on:click="exitModal">확인</div>
  </div>
</template>
<script
  type="text/javascript"
  src="//dapi.kakao.com/v2/maps/sdk.js?appkey=69d0c2177d4e8cf1a0f7361daafcc7ac&libraries=services"
></script>
<script>
import axios from "axios";
import { stringify } from "querystring";

export default {
  name: "modalMap",
  components: {},
  data() {
    return {
      address: "",
      btnText: "여기에요!",
      bgColor: "white",
      addinput: "",
      Lx: "",
      Ly: "",
    };
  },
  methods: {
    exitModal() {
      this.$store.state.showModal = false
    },
  },
  computed: {
    locX() {
      return this.$store.state.locationX;
    },
    locY() {
      return this.$store.state.locationY;
    },
  },
  mounted() {
    var mapContainer = document.getElementById("map"), // 지도를 표시할 div
      mapOption = {
        center: new kakao.maps.LatLng(this.locY, this.locX), // 지도의 중심좌표
        level: 3, // 지도의 확대 레벨
      };

    // 지도를 표시할 div와  지도 옵션으로  지도를 생성합니다
    var map = new kakao.maps.Map(mapContainer, mapOption);
    var marker = new kakao.maps.Marker({
      // 지도 중심좌표에 마커를 생성합니다
      position: map.getCenter(),
    });

    marker.setMap(map);
  },
};
</script>
<style scoped>
.confirm {
  width: 30%;
  padding: 0.5em;
  margin: 1em;
  margin-bottom: 1em;
  font-size: 1.25em;
  border: 1px solid #5d5d5d;
  border-radius: 20px;
  color: black;
  background-color: white;
}

.confirm:hover {
  box-shadow: 2px 2px 10px 0 grey;
  border: 1px solid #ebebeb;
  border-radius: 20px;
  outline: none;
}
.confirm:active {
  box-shadow: inset 0 0 5px grey;
  border: 1px solid #ebebeb;
  outline: none;
}

.mapapp-container {
  top: 0;
  left: 0;
  position: relative;
  text-align: center;
}
#map {
  z-index: 5;
}
.search-map {
  position: relative;
  width: 100%;
  height: 40vh;
  margin-bottom: 20px;
}

.modal-map-wrapper {
  /* position */
  position: fixed;
  top: 32%;
  right: 5%;

  /* modal shape */
  height: 40%;
  width: 20%;
  border: 1px solid black;
  /* border-radius: 15px; */

  /* content */
  background-color: ghostwhite;
  color: black;
  font-size: 1rem;

  justify-content: space-between;
  align-items: center;
  display: flex;
  flex-direction: column;
}

.modal-map-container {
  width: 100%;
  height: 100%;
}

.modal-map-collide {
  position: absolute;
  top: 0;
  right: 0;
  border: none;
  background: transparent;
  font-size: 40px;
  z-index: 6;
}
</style>
