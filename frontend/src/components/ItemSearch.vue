<script lang="ts">
export default {
  props: ["item"],
  data() {
    return {
      map: Location,
    };
  },
  mounted() {
    this.updateMap(this.item.longitude, this.item.latitude);
    console.log(this.item.longitude, this.item.latitude);
  },
  methods: {
    updateMap(longitude: any, latitude: any) {
      // eslint-disable-next-line no-undef
      var redIcon = new L.Icon({
        iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowSize: [41, 41]
      });
      var map = L.map("map").setView([latitude,longitude], 15);
      var marker = L.marker([latitude, longitude],{icon:redIcon}).addTo(map);
      // eslint-disable-next-line no-undef
      L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution:
          '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
      }).addTo(map);
    },
  },
};
</script>

<template>
  <div class="p-4">
    <h3 class="result text-center">Hasil Pencarian</h3>
    <div class="row align-items-center p-2">
      <div class="col-3 align-items-center">
        <div id="map"></div>
      </div>
      <div class="col-6 my-2">
        <div class="row result">
          <div class="col-5 text-right">Nama</div>
          <div class="col-1">:</div>
          <div class="col-6">{{ item.name }}</div>
        </div>
        
        <div class="row result">
          <div class="col-5">ND Internet</div>
          <div class="col-1">:</div>
          <div class="col-6">{{ item.NDInternet }}</div>
        </div>
        <div class="row result">
          <div class="col-5">SN ONT</div>
          <div class="col-1">:</div>
          <div class="col-6">{{ item.SNONT }}</div>
        </div>
        <div class="row result">
          <div class="col-5">Alamat</div>
          <div class="col-1">:</div>
          <div class="col-6">{{ item.alamat }}</div>
        </div>
        <div class="row result">
          <div class="col-5">Tikor</div>
          <div class="col-1">:</div>
          <div class="col-6">{{ `${item.longitude}, ${item.latitude}` }}</div>
        </div>
        <div class="row result">
          <div class="col-5">ODP</div>
          <div class="col-1">:</div>
          <div class="col-6">{{ item.ODP }}</div>
        </div>
      </div>
      <div class="col-3 text-center my-5 result">
        <h5>History ONT</h5>
        <div class="row result">
          <div class="col-6 bg-light text-dark">First ONT</div>
          <div class="col-6 bg-light text-dark">{{ item.firstONT }}</div>
        </div>
        <div class="row result">
          <div class="col-6 bg-white text-dark">Last ONT</div>
          <div class="col-6 bg-white text-dark">{{ item.lastONT }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.result {
  color: white;
  font-weight: 500;
}
#map {
  height: 250px;
}
</style>
