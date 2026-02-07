import React, { useState } from 'react';
import RecipeCard from '../components/RecipeCard';

const RecipesPage = () => {
  const [activeFilter, setActiveFilter] = useState('all');
  
  // 模拟数据
  const recipes = [
    { id: 1, name: '金汤力', difficulty: 'easy', prepTime: 5, rating: 4.5, isIbaOfficial: true, canMake: true },
    { id: 2, name: '莫吉托', difficulty: 'medium', prepTime: 10, rating: 4.8, isIbaOfficial: true, canMake: true },
    { id: 3, name: '古典鸡尾酒', difficulty: 'medium', prepTime: 8, rating: 4.3, isIbaOfficial: true, canMake: false },
    { id: 4, name: '玛格丽特', difficulty: 'medium', prepTime: 7, rating: 4.6, isIbaOfficial: true, canMake: true },
    { id: 5, name: '血腥玛丽', difficulty: 'hard', prepTime: 15, rating: 4.2, isIbaOfficial: true, canMake: false },
  ];

  const filters = [
    { id: 'all', label: '全部配方' },
    { id: 'available', label: '可制作' },
    { id: 'iba', label: 'IBA官方' },
    { id: 'easy', label: '简单难度' },
  ];

  const filteredRecipes = recipes.filter(recipe => {
    if (activeFilter === 'available') return recipe.canMake;
    if (activeFilter === 'iba') return recipe.isIbaOfficial;
    if (activeFilter === 'easy') return recipe.difficulty === 'easy';
    return true;
  });

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">配方库</h1>
          <p className="text-gray-600 mt-2">探索经典与创新的调酒配方</p>
        </div>
        <button className="btn-primary flex items-center">
          <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
          </svg>
          添加配方
        </button>
      </div>

      {/* 过滤选项 */}
      <div className="mb-6">
        <div className="flex flex-wrap gap-2">
          {filters.map((filter) => (
            <button
              key={filter.id}
              onClick={() => setActiveFilter(filter.id)}
              className={`px-4 py-2 rounded-lg ${
                activeFilter === filter.id
                  ? 'bg-primary-600 text-white'
                  : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
              }`}
            >
              {filter.label}
            </button>
          ))}
        </div>
      </div>

      {/* 配方列表 */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {filteredRecipes.map((recipe) => (
          <RecipeCard key={recipe.id} recipe={recipe} />
        ))}
      </div>

      {filteredRecipes.length === 0 && (
        <div className="text-center py-12">
          <svg className="w-16 h-16 mx-auto text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
          </svg>
          <h3 className="mt-4 text-lg font-medium text-gray-900">暂无配方</h3>
          <p className="mt-2 text-gray-600">添加您的第一个配方来开始吧！</p>
          <button className="mt-4 btn-primary">
            添加配方
          </button>
        </div>
      )}
    </div>
  );
};

export default RecipesPage;