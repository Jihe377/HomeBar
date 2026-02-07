import React from 'react';
import { Link } from 'react-router-dom';

const RecipeCard = ({ recipe }) => {
  const getDifficultyColor = (difficulty) => {
    const colors = {
      easy: 'bg-green-100 text-green-800',
      medium: 'bg-yellow-100 text-yellow-800',
      hard: 'bg-red-100 text-red-800',
    };
    return colors[difficulty] || colors.medium;
  };

  const getDifficultyLabel = (difficulty) => {
    const labels = {
      easy: '简单',
      medium: '中等',
      hard: '困难',
    };
    return labels[difficulty] || '中等';
  };

  return (
    <div className="card hover:shadow-lg transition-shadow">
      <div className="flex justify-between items-start mb-4">
        <div>
          <h3 className="text-xl font-bold text-gray-900">{recipe.name}</h3>
          <div className="flex items-center mt-1">
            <svg className="w-4 h-4 text-yellow-400 mr-1" fill="currentColor" viewBox="0 0 20 20">
              <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
            </svg>
            <span className="text-gray-700">{recipe.rating}</span>
            <span className="text-gray-500 text-sm ml-1">({recipe.ratingCount || 0})</span>
          </div>
        </div>
        <div className="flex flex-col items-end space-y-2">
          <span className={`px-3 py-1 rounded-full text-sm font-medium ${getDifficultyColor(recipe.difficulty)}`}>
            {getDifficultyLabel(recipe.difficulty)}
          </span>
          {recipe.isIbaOfficial && (
            <span className="px-2 py-1 bg-blue-100 text-blue-800 text-xs font-medium rounded">
              IBA官方
            </span>
          )}
        </div>
      </div>

      {/* 配方信息 */}
      <div className="space-y-3 mb-6">
        <div className="flex items-center text-gray-600">
          <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <span>准备时间：{recipe.prepTime}分钟</span>
        </div>
        
        <div className="flex items-center">
          <div className={`flex items-center px-3 py-1 rounded-lg ${recipe.canMake ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
            <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d={recipe.canMake ? "M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" : "M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"} />
            </svg>
            {recipe.canMake ? '可制作' : '材料不足'}
          </div>
        </div>
      </div>

      {/* 操作按钮 */}
      <div className="flex space-x-2">
        <Link
          to={`/recipes/${recipe.id}`}
          className="flex-1 btn-primary text-center py-2"
        >
          查看详情
        </Link>
        <button className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50">
          <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" />
          </svg>
        </button>
      </div>
    </div>
  );
};

export default RecipeCard;