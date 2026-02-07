import React, { useState } from 'react';

const BarItemForm = ({ onSubmit, onCancel, initialData }) => {
  const [formData, setFormData] = useState(initialData || {
    name: '',
    category: 'spirit',
    brand: '',
    volume: '',
    currentVolume: '',
    abv: '',
    description: '',
    isAvailable: true,
  });

  const categories = [
    { value: 'spirit', label: '基酒' },
    { value: 'liqueur', label: '利口酒' },
    { value: 'wine', label: '葡萄酒' },
    { value: 'beer', label: '啤酒' },
    { value: 'mixer', label: '调酒饮料' },
    { value: 'fruit', label: '水果' },
    { value: 'herb', label: '香草' },
    { value: 'other', label: '其他' },
  ];

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === 'checkbox' ? checked : value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* 名称 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            物品名称 *
          </label>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
            className="input-field"
            placeholder="例如：金酒、柠檬汁"
          />
        </div>

        {/* 分类 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            分类 *
          </label>
          <select
            name="category"
            value={formData.category}
            onChange={handleChange}
            className="input-field"
          >
            {categories.map((cat) => (
              <option key={cat.value} value={cat.value}>
                {cat.label}
              </option>
            ))}
          </select>
        </div>

        {/* 品牌 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            品牌
          </label>
          <input
            type="text"
            name="brand"
            value={formData.brand}
            onChange={handleChange}
            className="input-field"
            placeholder="例如：Gordon's、Bacardi"
          />
        </div>

        {/* 酒精度 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            酒精度（%）
          </label>
          <input
            type="number"
            name="abv"
            value={formData.abv}
            onChange={handleChange}
            min="0"
            max="100"
            step="0.1"
            className="input-field"
            placeholder="例如：40"
          />
        </div>

        {/* 总容量 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            总容量（ml） *
          </label>
          <input
            type="number"
            name="volume"
            value={formData.volume}
            onChange={handleChange}
            required
            min="0"
            className="input-field"
            placeholder="例如：750"
          />
        </div>

        {/* 当前容量 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            当前剩余容量（ml） *
          </label>
          <input
            type="number"
            name="currentVolume"
            value={formData.currentVolume}
            onChange={handleChange}
            required
            min="0"
            max={formData.volume || 9999}
            className="input-field"
            placeholder="例如：500"
          />
        </div>
      </div>

      {/* 描述 */}
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          描述
        </label>
        <textarea
          name="description"
          value={formData.description}
          onChange={handleChange}
          rows="3"
          className="input-field"
          placeholder="添加备注（如：产地、风味特点）"
        />
      </div>

      {/* 可用性 */}
      <div className="flex items-center">
        <input
          type="checkbox"
          id="isAvailable"
          name="isAvailable"
          checked={formData.isAvailable}
          onChange={handleChange}
          className="h-4 w-4 text-primary-600 rounded"
        />
        <label htmlFor="isAvailable" className="ml-2 text-sm text-gray-700">
          物品可用（如果不可用，将不计入可制作配方）
        </label>
      </div>

      {/* 按钮 */}
      <div className="flex justify-end space-x-4 pt-6 border-t">
        <button
          type="button"
          onClick={onCancel}
          className="btn-secondary"
        >
          取消
        </button>
        <button
          type="submit"
          className="btn-primary"
        >
          {initialData ? '更新物品' : '添加物品'}
        </button>
      </div>
    </form>
  );
};

export default BarItemForm;