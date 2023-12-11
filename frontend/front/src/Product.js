import React, {useState, useEffect } from 'react';
import axios from 'axios'
import { Link, useParams} from 'react-router-dom';


function ProductList() {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/v1/products/product/')
        .then(response => {
            setProducts(response.data);

        })
        .catch(err => {
            console.log(err);
        });

    }, []);
  return (
    <div  style={{ width: '290px'}}>
      <h1>Список продуктов</h1>
      <ul>
        {products.map((product) => (
          <li key={product.id} style={{border: '1px solid #333',
                                       padding: '10px 50px',
                                       margin: '10px'}}>
            <p>Name: {product.name}</p>
            <p>Price: {product.price}$</p>
            <p>Category: {product.category_name}</p>
            <Link to={'/products/${product.slug}'}>more...</Link>

          </li>


        ))}
      </ul>
    </div>
  );
}

function ProductDetail() {
    const [product, setProduct] = useState({});
    const {slug} = useParams();

    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/api/v1/products/product/${slug}`)
        .then(response => {
            setProduct(response.data);
        })
        .catch(err => {
            console.log(err);
        });

    }, [slug]);
  return (
    <div  style={{width: '290px',
                  border: '1px solid #333',
                  padding: '10px 50px',
                  margin: '10px'}}>
      <h1>Делати продукта</h1>
      <p>Name: {product.name}</p>
      <p>Description: {product.description}</p>
      <p>Price: {product.price}</p>
    </div>
  );
}

export {ProductList, ProductDetail};
