<script lang="ts">
import axios from "axios";
import Swal from "sweetalert2";

export default {
    data(){
        return {
        file: ''
        }
    },
    methods: {
      /*
        Submits the file to the server
      */
      submitFile(){
        /*
                Initialize the form data
            */
            let formData = new FormData();

            /*
                Add the form data we need to submit
            */
            formData.append('file', this.file);

            axios.post( 'http://localhost:5000/odp/',
                formData,
                {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
              }
            ).then((response) => {
            Swal.fire("Success!", "Berhasil menambahkan data", "success");
        })
        .catch((error) => {
          Swal.fire(
            "Failed!",
            error.response.data.error
              ? `${error.response.data.error} (${error.response.status})`
              : `Request gagal tanpa error message (${error.response.status})`,
            "error"
          );
          console.log(error);
        });
      },

      /*
        Handles a change on the file upload
      */
      handleFileUpload(){
        this.file = this.$refs.file.files[0];
      }
    }
  }
</script>

<template>
    <div class="input-page">
        <div class="container shadow rounded p-4">
            <div class="row g-3 align-items center mt-2">
                <h3 class="text-center">
                 <strong>Input ODP</strong>
                </h3>
            </div>
            <div class="row g-3 align-items-center mt-2">
                <div class="col-2"></div>
                <div class="col-4">
                    <label for="odp" class="col-form-label">Masukan File ODP</label>
                </div>
                <div class="col-6">
                    <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
                </div>
            </div>
            <div class="row g-3 align-items-center mt-2">
                <div class="col-3"></div>
                <div class="col-6 text-center">
                    <button @click="submitFile()" class="btn btn-primary">Submit</button>
                </div>
            </div>
            <div class="row align-items-center mt-3 mx-5">
              <div class="col">
                <embed src="public/panduan.pdf" width="100%" height="400px" />
              </div>
            </div>
        </div>
    </div>
  </template>
  
  <style>
  @media (min-width: 1024px) {
    .search-page {
      min-height: 100vh;
      display: flex;
      align-items: center;
    }
  }
  </style>
  