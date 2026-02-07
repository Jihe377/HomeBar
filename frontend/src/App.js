import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Layout from './components/Layout';
import Dashboard from './pages/Dashboard';
import BarItemsPage from './pages/BarItemsPage';
import RecipesPage from './pages/RecipesPage';
import CocktailRecordsPage from './pages/CocktailRecordsPage';
import ShoppingListPage from './pages/ShoppingListPage';
import PreferencesPage from './pages/PreferencesPage';

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/bar-items" element={<BarItemsPage />} />
          <Route path="/recipes" element={<RecipesPage />} />
          <Route path="/cocktail-records" element={<CocktailRecordsPage />} />
          <Route path="/shopping-list" element={<ShoppingListPage />} />
          <Route path="/preferences" element={<PreferencesPage />} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;