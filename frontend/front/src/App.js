import logo from './logo.svg';
import './App.css';
import {ProductList, ProductDetail} from './Product';
import { BrowserRouter as Router, Link, Routes, Route } from 'react-router-dom';


function App() {
  return (
    <Router>
        <Routes>
            <Route path='/products' element={<ProductList />} />
            <Route path='/products/:slug' element={<ProductDetail />} />
        </Routes>
    </Router>
  );
}

export default App;
