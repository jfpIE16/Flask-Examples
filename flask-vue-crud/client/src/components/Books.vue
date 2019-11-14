<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Biblioteca</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.book-modal>Add Book</button> 
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Titulo</th>
              <th scope="col">Autor</th>
              <th scope="col">Genero</th>
              <th scope="col">Disponibilidad</th>
              
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.title }}</td>
              <td>{{ book.genre }}</td>
              <td>{{ book.author }}</td>
              <td>
                  <span v-if="book.available">Si</span>
                  <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Actualizar</button>
                  <button type="button" class="btn btn-danger btn-sm">Eliminar</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addBookModal"
            id="book-modal"
            title="Add a new book"
            hide-footer>
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
    <b-form-group id="form-title-group"
                    label="Titulo:"
                    label-for="form-title-input">
        <b-form-input id="form-title-input"
                        type="text"
                        v-model="addBookForm.title"
                        required
                        placeholder="Ingrese titulo">
        </b-form-input>
    </b-form-group>
    <b-form-group id="form-author-group"
                    label="Autor:"
                    label-for="form-author-input">
            <b-form-input id="form-author-input"
                        type="text"
                        v-model="addBookForm.author"
                        required
                        placeholder="Ingrese autor">
            </b-form-input>
    </b-form-group>
    <b-form-group id="form-genre-group"
                    label="Genero:"
                    label-for="form-genre-input">
            <b-form-input id="form-genre-input"
                        type="text"
                        v-model="addBookForm.genre"
                        required
                        placeholder="Ingrese genero">
            </b-form-input>
    </b-form-group>
    <b-form-group id="form-read-group">
        <b-form-checkbox-group v-model="addBookForm.available" id="form-checks">
            <b-form-checkbox value="true">Available?</b-form-checkbox>
        </b-form-checkbox-group>
    </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
    </b-modal>
  </div>
  
</template>


<script>
import axios from 'axios';
export default {
    data(){
        return {
            books: [],
            addBookForm: {
                title: '',
                author: '',
                genre: '',
                available: [],
            },
        };
    },

    methods: {
        getBooks(){
            const path = 'http://localhost:5000/books';
            axios.get(path)
                .then((res) => {
                    this.books = res.data.books;
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });
        },
        addBook(payload){
            const path = 'http://localhost:5000/books';
            axios.post(path, payload)
                .then(() => {
                    this.getBooks();
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.log(error);
                    this.getBooks();
                });
        },
        initForm(){
            this.addBookForm.title = '';
            this.addBookForm.author = '';
            this.addBookForm.genre = '';
            this.addBookForm.available = [];
        },
        onSubmit(evt){
            evt.preventDefault();
            this.$refs.addBookModal.hide();
            let available = false;
            if(this.addBookForm.available[0]) available = true;
            const payload = {
                title: this.addBookForm.title,
                author: this.addBookForm.author,
                genre: this.addBookForm.genre,
                available
            };
            this.addBook(payload);
            this.initForm();
        },
        onReset(evt){
            evt.preventDefault();
            this.$refs.addBookModal.hide();
            this.initForm();
        },
    },
    created(){
        this.getBooks();
    },
};
</script>