<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Biblioteca</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.book-modal>Agregar Libro</button> 
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
                  <button 
                    type="button" 
                    class="btn btn-warning btn-sm"
                    v-b-modal.book-update-modal
                    @click="editBook(book)">Actualizar</button>
                  <button 
                    type="button" 
                    class="btn btn-danger btn-sm"
                    @click="onDeleteBook(book)">Eliminar</button>
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
          <b-button type="submit" variant="primary">Agregar</b-button>
          <b-button type="reset" variant="danger">Cancelar</b-button>
      </b-form>
    </b-modal>
    <b-modal ref="editBookModal"
         id="book-update-modal"
         title="Actualizar"
         hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-title-edit-group"
                    label="Titulo:"
                    label-for="form-title-edit-input">
          <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="editForm.title"
                        required
                        placeholder="Ingrese Titulo">
          </b-form-input>
      </b-form-group>
      <b-form-group id="form-author-edit-group"
                      label="Autor:"
                      label-for="form-author-edit-input">
          <b-form-input id="form-author-edit-input"
                          type="text"
                          v-model="editForm.author"
                          required
                          placeholder="Ingrese Autor">
          </b-form-input>
      </b-form-group>
      <b-form-group id="form-genre-edit-group"
                      label="Género:"
                      label-for="form-genre-edit-input">
          <b-form-input id="form-genre-edit-input"
                          type="text"
                          v-model="editForm.genre"
                          required
                          placeholder="Ingrese Género">
          </b-form-input>
      </b-form-group>
      <b-form-group id="form-read-edit-group">
          <b-form-checkbox-group v-model="editForm.available" id="form-checks">
            <b-form-checkbox value="true">Disponible?</b-form-checkbox>
          </b-form-checkbox-group>
      </b-form-group>
      <b-button-group>
          <b-button type="submit" variant="primary">Actualizar</b-button>
          <b-button type="reset" variant="danger">Cancelar</b-button>
      </b-button-group>
      </b-form>
    </b-modal>
  </div>
  
</template>


<script>
import axios from 'axios';
import Alert from './Alert.vue';
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
            message: '',
            showMessage: false,
            editForm: {
                id: '',
                title: '',
                author: '',
                genre: '',
                available: [],
            },
        };
    },
    components: {
      alert: Alert,
    },
    methods: {
        getBooks(){
            const path = 'http://localhost:5000/books';
            axios.get(path)
                .then((res) => {
                    this.books = res.data.books;
                    if(this.books.length == 0){
                      this.message = "No hay libros, agrega uno!"
                      this.showMessage = true;
                    }
                    
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
                    this.message = "Libro agregado!";
                    this.showMessage = true;
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
            this.editBookForm.title = '';
            this.editBookForm.author = '';
            this.editBookForm.genre = '';
            this.editBookForm.available = [];
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
        editBook(book){
          this.editForm = book;
        },
        onSubmitUpdate(evt){
            evt.preventDefault();
            this.$refs.editBookModal.hide();
            let available = false;
            if (this.editForm.available[0]) available = true;
            const payload = {
              title: this.editForm.title,
              author: this.editForm.author,
              genre: this.editForm.genre,
              available,
            };
            this.updateBook(payload, this.editForm.id);
        },
        updateBook(payload, bookID){
          const path = `http://localhost:5000/books/${bookID}`;
          axios.put(path, payload)
            .then(() => {
              this.getBooks();
              this.message = 'Libro actualizado!';
              this.showMessage = true;
            })
            .catch((error) => {
              //eslint-disable-next-line
              console.error(error);
              this.getBooks();
            });
        },
        onResetUpdate(evt){
          evt.preventDefault();
          this.$refs.editBookModal.hide();
          this.initForm();
          this.getBooks();
        },
        removeBook(bookID){
          const path = `http://localhost:5000/books/${bookID}`;
          axios.delete(path)
            .then(() => {
              this.getBooks();
              this.message = "Libro eliminado!";
              this.showMessage = true;
            })
            .catch((error) => {
              //eslint-disable-next-line
              console.error(error);
              this.getBooks();
            });
        },
        onDeleteBook(book){
          this.removeBook(book.id);
        },
    },
    created(){
        this.getBooks();
    },
};
</script>