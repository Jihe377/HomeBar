import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || '/api/v1';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// 请求拦截器
api.interceptors.request.use(
  (config) => {
    // 可以在这里添加认证token
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// 响应拦截器
api.interceptors.response.use(
  (response) => response.data,
  (error) => {
    console.error('API Error:', error.response?.data || error.message);
    return Promise.reject(error.response?.data || error.message);
  }
);

// 酒柜物品API
export const barItemsAPI = {
  getAll: (params) => api.get('/bar-items', { params }),
  getById: (id) => api.get(`/bar-items/${id}`),
  create: (data) => api.post('/bar-items', data),
  update: (id, data) => api.put(`/bar-items/${id}`, data),
  delete: (id) => api.delete(`/bar-items/${id}`),
};

// 配方API
export const recipesAPI = {
  getAll: (params) => api.get('/recipes', { params }),
  getById: (id) => api.get(`/recipes/${id}`),
  create: (data) => api.post('/recipes', data),
  update: (id, data) => api.put(`/recipes/${id}`, data),
  delete: (id) => api.delete(`/recipes/${id}`),
  getAvailable: (params) => api.get('/recipes/available', { params }),
  checkAvailability: (id) => api.get(`/recipes/${id}/availability`),
};

// 调酒记录API
export const cocktailRecordsAPI = {
  getAll: (params) => api.get('/cocktail-records', { params }),
  getById: (id) => api.get(`/cocktail-records/${id}`),
  create: (data) => api.post('/cocktail-records', data),
  update: (id, data) => api.put(`/cocktail-records/${id}`, data),
  delete: (id) => api.delete(`/cocktail-records/${id}`),
};

// 购物清单API
export const shoppingAPI = {
  getAll: (params) => api.get('/shopping', { params }),
  getById: (id) => api.get(`/shopping/${id}`),
  create: (data) => api.post('/shopping', data),
  update: (id, data) => api.put(`/shopping/${id}`, data),
  delete: (id) => api.delete(`/shopping/${id}`),
  createFromRecipe: (recipeId) => api.post(`/shopping/from-recipe/${recipeId}`),
};

// 口味偏好API
export const preferencesAPI = {
  get: (sessionId) => api.get(`/preferences/${sessionId}`),
  create: (data) => api.post('/preferences', data),
  update: (sessionId, data) => api.put(`/preferences/${sessionId}`, data),
  delete: (sessionId) => api.delete(`/preferences/${sessionId}`),
};

// 标签API
export const tagsAPI = {
  getAll: (params) => api.get('/tags', { params }),
  getById: (id) => api.get(`/tags/${id}`),
  create: (data) => api.post('/tags', data),
  delete: (id) => api.delete(`/tags/${id}`),
};

// 工具API
export const utilsAPI = {
  checkAllAvailability: (params) => api.get('/utils/check-availability', { params }),
  generateShoppingList: (recipeIds) => api.get('/utils/generate-shopping-list', { params: { recipe_ids: recipeIds } }),
};

export default api;