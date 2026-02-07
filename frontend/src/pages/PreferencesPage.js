import React, { useState } from 'react';

const PreferencesPage = () => {
  const [preferences, setPreferences] = useState({
    flavors: ['sweet', 'fruity'],
    strength: 0.6,
    sweetness: 0.7,
    sourness: 0.4,
    excludeIngredients: ['cilantro'],
  });

  const flavorOptions = [
    { id: 'sweet', label: '甜', color: 'bg-pink-100 text-pink-800' },
    { id: 'sour', label: '酸', color: 'bg-yellow-100 text-yellow-800' },
    { id: 'bitter', label: '苦', color: 'bg-amber-100 text-amber-800' },
    { id: 'fruity', label: '果味', color: 'bg-red-100 text-red-800' },
    { id: 'herbal', label: '草本', color: 'bg-green-100 text-green-800' },
    { id: 'spicy', label: '辛辣', color: 'bg-orange-100 text-orange-800' },
    { id: 'smoky', label: '烟熏', color: 'bg-gray-100 text-gray-800' },
    { id: 'refreshing', label: '清爽', color: 'bg-blue-100 text-blue-800' },
    { id: 'strong', label: '烈', color: 'bg-purple-100 text-purple-800' },
  ];

  const handleFlavorToggle = (flavorId) => {
    setPreferences(prev => {
      const newFlavors = prev.flavors.includes(flavorId)
        ? prev.flavors.filter(f => f !== flavorId)
        : [...prev.flavors, flavorId];
      return { ...prev, flavors: newFlavors };
    });
  };

  const handleSliderChange = (key, value) => {
    setPreferences(prev => ({ ...prev, [key]: parseFloat(value) }));
  };

  const handleSave = () => {
    console.log('保存偏好:', preferences);
    // 这里应该调用API
    alert('偏好设置已保存！');
  };

  return (
    <div>
      <div className="mb-6">
        <h1 className="text-3xl font-bold text-gray-900">口味偏好</h1>
        <p className="text-gray-600 mt-2">设置您的口味偏好，获取个性化推荐</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* 口味偏好 */}
        <div className="card">
          <h2 className="text-xl font-bold mb-6">偏好口味</h2>
          <div className="space-y-4">
            <p className="text-gray-600">选择您喜欢的口味（可多选）：</p>
            <div className="flex flex-wrap gap-3">
              {flavorOptions.map((flavor) => (
                <button
                  key={flavor.id}
                  onClick={() => handleFlavorToggle(flavor.id)}
                  className={`px-4 py-2 rounded-lg transition-colors ${
                    preferences.flavors.includes(flavor.id)
                      ? `${flavor.color} ring-2 ring-offset-2 ring-opacity-50`
                      : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                  }`}
                >
                  {flavor.label}
                </button>
              ))}
            </div>
          </div>
        </div>

        {/* 强度偏好 */}
        <div className="card">
          <h2 className="text-xl font-bold mb-6">强度偏好</h2>
          <div className="space-y-6">
            <div>
              <div className="flex justify-between mb-2">
                <label className="text-gray-700">酒精度偏好</label>
                <span className="font-medium">{Math.round(preferences.strength * 100)}%</span>
              </div>
              <input
                type="range"
                min="0"
                max="1"
                step="0.1"
                value={preferences.strength}
                onChange={(e) => handleSliderChange('strength', e.target.value)}
                className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
              />
              <div className="flex justify-between text-xs text-gray-500 mt-1">
                <span>清淡</span>
                <span>中等</span>
                <span>浓烈</span>
              </div>
            </div>

            <div>
              <div className="flex justify-between mb-2">
                <label className="text-gray-700">甜度偏好</label>
                <span className="font-medium">{Math.round(preferences.sweetness * 100)}%</span>
              </div>
              <input
                type="range"
                min="0"
                max="1"
                step="0.1"
                value={preferences.sweetness}
                onChange={(e) => handleSliderChange('sweetness', e.target.value)}
                className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
              />
              <div className="flex justify-between text-xs text-gray-500 mt-1">
                <span>不甜</span>
                <span>适中</span>
                <span>很甜</span>
              </div>
            </div>

            <div>
              <div className="flex justify-between mb-2">
                <label className="text-gray-700">酸度偏好</label>
                <span className="font-medium">{Math.round(preferences.sourness * 100)}%</span>
              </div>
              <input
                type="range"
                min="0"
                max="1"
                step="0.1"
                value={preferences.sourness}
                onChange={(e) => handleSliderChange('sourness', e.target.value)}
                className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
              />
              <div className="flex justify-between text-xs text-gray-500 mt-1">
                <span>不酸</span>
                <span>适中</span>
                <span>很酸</span>
              </div>
            </div>
          </div>
        </div>

        {/* 排除成分 */}
        <div className="card lg:col-span-2">
          <h2 className="text-xl font-bold mb-6">排除成分</h2>
          <div className="space-y-4">
            <p className="text-gray-600">输入您不喜欢的成分（用逗号分隔）：</p>
            <textarea
              value={preferences.excludeIngredients.join(', ')}
              onChange={(e) => setPreferences(prev => ({
                ...prev,
                excludeIngredients: e.target.value.split(',').map(item => item.trim()).filter(Boolean)
              }))}
              rows="3"
              className="input-field"
              placeholder="例如：香菜、八角、肉桂"
            />
            <p className="text-sm text-gray-500">
              系统将避免推荐包含这些成分的配方。
            </p>
          </div>
        </div>
      </div>

      {/* 保存按钮 */}
      <div className="mt-8 flex justify-end">
        <button
          onClick={handleSave}
          className="btn-primary px-8 py-3"
        >
          保存偏好设置
        </button>
      </div>

      {/* 提示 */}
      <div className="mt-8 p-4 bg-primary-50 rounded-lg">
        <h3 className="font-medium text-primary-900 mb-2">如何工作？</h3>
        <ul className="text-sm text-primary-700 space-y-1">
          <li>• 系统会根据您的口味偏好推荐合适的配方</li>
          <li>• 在您记录调酒评价时，系统会学习您的偏好</li>
          <li>• 这些设置仅用于个性化推荐，不会影响基础功能</li>
        </ul>
      </div>
    </div>
  );
};

export default PreferencesPage;