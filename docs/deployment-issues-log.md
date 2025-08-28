# Hugo 网站部署问题实战记录

## 背景
从稳定运行的commit `8235b6f`开始，尝试添加两篇研究论文到个人学术网站，但遇到了一系列复杂的部署和稳定性问题。

## 问题发现过程

### 初始稳定状态
- **Commit**: `8235b6f` - "更新assets/media/matrix-transform-bg.html原点位置"
- **状态**: 网站可以长期稳定运行
- **特征**: 基础Hugo Blox Builder academic主题，包含模板内容

### 第一轮问题 - 复杂内容导致的系统过载

#### 症状
- **部署时间异常**: 6分17秒（正常应该在1-2分钟内）
- **运行模式**: 部署成功后运行约10分钟然后崩溃
- **错误表现**: "白底蓝字只有几个标题的错误页面"

#### 初步分析和尝试的修复
1. **YAML语法问题**: 发现abstract中有未转义引号，修改为multiline格式
2. **文件冲突**: 每个publication同时存在featured.png和featured.jpg
3. **模板隐藏**: 使用draft: true隐藏模板占位符
4. **Featured过载**: 同时有4个featured: true项目

#### 错误的解决路径
- 频繁修改YAML格式（单行→多行→单行）
- 删除"冲突"文件
- 多次commit试图修复症状而非根因

### 关键发现 - "蓝色标题"现象

#### 现象描述
- 网站部署完成后**立即**显示"蓝色标题，没有正确加载内容"
- 不是运行一段时间后崩溃，而是从一开始就无法正确渲染
- 这表明整个网站结构都挂了，不仅仅是CSS问题

#### 确定根因的实验
通过删除我们添加的两个publication目录：
```bash
rm -rf content/publication/compliance-to-code 
rm -rf content/publication/fedspeak-confidence
```
**结果**: 网站立即恢复正常

#### 结论
**问题出在我们添加的publication内容本身，而不是配置、冲突或资源过载问题。**

## 技术分析

### 可能的根本原因
1. **Hugo版本兼容性**: 我们的YAML frontmatter格式可能与当前Hugo版本不兼容
2. **必需字段缺失**: publication类型可能需要特定的必需字段
3. **数据类型错误**: 某些字段的数据格式不符合Hugo schema要求
4. **编码问题**: 文件编码或特殊字符导致解析失败

### 排除的因素
- ❌ 文件大小或内容复杂度
- ❌ 图片文件冲突  
- ❌ Featured publications数量
- ❌ 部署资源限制
- ❌ CSS/主题加载问题

## 当前状态

### 实验设置
- **当前Commit**: `862cd46` - 包含简化版publications
- **观察期**: 正在观察网站稳定性
- **预期**: 如果简化版本仍有问题，说明是基本的YAML结构问题

### 待验证假设
1. **最小化内容是否有效**: 当前简化版本能否稳定运行
2. **特定字段问题**: 是否某个字段格式导致Hugo解析失败
3. **逐步添加内容**: 确定哪个具体元素导致问题

## 经验教训

### 问题诊断方法
1. **✅ 对比删除法**: 通过删除怀疑内容确认根因最有效
2. **❌ 症状修复**: 修改配置试图解决表面症状是错误路径
3. **✅ 基线回归**: 保持已知稳定状态作为对照组

### Git工作流改进
1. **分支策略**: 应该用feature分支进行实验性修改
2. **渐进提交**: 每次只修改一个要素，便于回滚
3. **文档同步**: 实时记录问题现象和修复尝试

### Hugo开发最佳实践
1. **YAML验证**: 使用YAML lint工具预先验证frontmatter
2. **模板对比**: 参考现有工作的publication模板
3. **本地测试**: 考虑本地Hugo环境进行初步验证

## 下一步行动计划

### 短期 (当前观察期)
- [ ] 监控当前简化版本的稳定性
- [ ] 如果仍有问题，进一步简化到最基本结构
- [ ] 确定最小可工作的publication模板

### 中期 (根因确定后)
- [ ] 逐步添加内容元素，确定具体问题字段
- [ ] 建立标准的publication添加检查清单
- [ ] 创建分支工作流模板

### 长期 (流程优化)
- [ ] 建立自动化检查工具
- [ ] 创建publication内容模板
- [ ] 文档化标准操作程序

## 成功案例分析 - 稳定运行一天后的发现

### 当前稳定状态 (Commit: 862cd46)
**运行时间**: 24小时+ 持续稳定运行  
**状态**: ✅ 正常显示所有内容，包括两篇研究论文

### 成功因素分析

#### 1. 保留模板占位符是关键
**重要发现**: 当前版本中模板占位符全部保留且正常显示：
- "An example conference paper" 
- "An example preprint / working paper"
- "An example journal article"

**错误假设的纠正**: 
- ❌ 之前假设：模板占位符导致featured publications过载
- ✅ 实际情况：删除模板占位符反而破坏了Hugo主题的结构完整性

#### 2. 内容长度是稳定性的决定因素
**当前工作版本的内容特征**:
```yaml
abstract: Regulatory compliance has become a cornerstone of corporate governance. We present Compliance-to-Code, the first large-scale Chinese dataset dedicated to financial regulatory compliance, covering 1,159 annotated clauses from 361 regulations. We also introduce FinCheck - a pipeline for automated compliance checking.
```
- **长度**: ~300字符
- **格式**: 单行YAML格式
- **内容**: 简洁的研究概述

**对比问题版本的内容**:
- **长度**: 1000+字符的完整研究描述
- **格式**: 多行YAML格式 (`abstract: >`)
- **内容**: 详细的技术细节和贡献列表

#### 3. YAML格式稳定性
**成功格式**:
```yaml
abstract: [简短单行内容]
```

**问题格式**:
```yaml
abstract: >
  [多行详细内容
   包含大量技术细节
   和复杂句式结构]
```

### 技术架构分析

#### Featured Publications处理能力
**当前状态**: 4个featured publications同时正常运行
- 2个模板占位符 (conference-paper, preprint) 
- 2个真实论文 (compliance-to-code, fedspeak-confidence)

**结论**: Hugo Blox Builder主题完全支持多个featured publications，数量不是限制因素。

#### 主题依赖结构
**模板占位符的作用**:
1. 提供CSS样式基准
2. 维护组件渲染的完整性
3. 确保Featured widget的正常工作

**经验**: 不应删除或隐藏模板内容，而应通过内容优化实现稳定性。

---

**记录时间**: 2025-08-28  
**最后更新**: 2025-08-29  
**当前状态**: ✅ 稳定运行24小时+  
**关键发现**: 内容长度和YAML格式是稳定性关键，模板占位符应保留