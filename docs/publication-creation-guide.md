# Hugo Blox Builder Publication 创建指南

## 必需文件和步骤

### 1. 目录结构
```
content/publication/your-paper-name/
├── index.md          # 必需：主要内容文件
├── featured.jpg      # 推荐：特色图片 (优先使用JPG格式)
└── cite.bib         # 可选：BibTeX引用信息
```

### 2. index.md 文件必需字段

基于Hugo Blox Builder模板要求，以下字段**必须存在**（即使为空）：

#### 核心信息字段
```yaml
---
title: '论文标题'
authors:
  - admin
  - 合作者姓名
author_notes:
  - 'Equal contribution'  # 或 '' 如果无特殊说明
  - ''
date: '2025-01-01T00:00:00Z'
doi: ''                    # 必需，即使为空
publishDate: '2025-01-01T00:00:00Z'
publication_types: ['paper-conference']
publication: In *会议或期刊名称*
publication_short: In *缩写*
abstract: 论文摘要内容
summary: 简短总结
```

#### 分类和展示字段
```yaml
tags:
  - 标签1
  - 标签2
featured: true    # 是否在首页展示
```

#### 链接字段（全部必需，即使为空）
```yaml
links:
  - name: ArXiv
    url: https://arxiv.org/abs/xxxx
url_pdf: 'PDF链接'
url_code: 'GitHub链接'
url_dataset: ''      # 必需存在
url_poster: ''       # 必需存在
url_project: ''      # 必需存在
url_slides: ''       # 必需存在
url_source: ''       # 必需存在
url_video: ''        # 必需存在
```

#### 图片和关联字段
```yaml
image:
  caption: '图片说明'
  focal_point: ''
  preview_only: false
projects: []         # 关联项目，通常为空
slides: ""          # 关联幻灯片，通常为空
---
```

### 3. 关键注意事项

#### YAML语法要求
1. **引号转义**：如果abstract中包含引号，需要正确转义
   ```yaml
   # 错误：
   abstract: "Fedspeak", the stylized language...
   
   # 正确：
   abstract: '"Fedspeak", the stylized language...'
   ```

2. **字段完整性**：所有URL字段必须存在，即使值为空字符串`''`

3. **数组对应**：`authors`和`author_notes`数组长度应对应

#### 特色图片要求
- **格式**：优先使用JPG格式，避免PNG/JPG文件冲突
- **命名**：必须命名为`featured.jpg`
- **位置**：放置在publication目录下

### 4. 最佳实践模板

创建新publication时，建议：

1. **复制现有模板**：
   ```bash
   cp -r content/publication/conference-paper content/publication/your-paper
   ```

2. **修改内容**：逐步修改字段，保持结构完整

3. **验证字段**：确保所有必需字段存在

4. **测试部署**：先提交基本版本，确认无误后添加详细内容

### 5. 常见错误和解决

| 错误现象 | 可能原因 | 解决方法 |
|---------|---------|---------|
| 蓝色标题，无内容 | 缺失必需字段 | 补充所有URL字段 |
| YAML解析错误 | 引号转义问题 | 检查abstract中的引号 |
| 图片不显示 | 文件名错误 | 确保使用`featured.jpg` |
| 网站崩溃 | 字段结构不完整 | 对比模板检查所有字段 |

### 6. 检查清单

创建新publication前的验证清单：

- [ ] 所有URL字段存在（即使为空）
- [ ] `author_notes`数组与`authors`对应
- [ ] `featured.jpg`图片文件存在
- [ ] Abstract中引号正确转义
- [ ] YAML语法验证通过
- [ ] 与现有模板字段结构一致

---

**重要提醒**：Hugo Blox Builder对字段结构要求严格，缺失任何必需字段都会导致渲染失败。建议严格按照现有模板结构创建新publication。