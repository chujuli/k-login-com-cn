from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import List, Optional


@dataclass
class KeywordNote:
    keyword: str
    source_url: str
    note: str
    created_at: datetime = field(default_factory=datetime.now)
    tags: List[str] = field(default_factory=list)
    priority: int = 1
    category: Optional[str] = None

    def to_simple_dict(self) -> dict:
        return {
            "keyword": self.keyword,
            "source_url": self.source_url,
            "note": self.note,
            "tags": self.tags,
            "priority": self.priority,
            "category": self.category,
        }

    def short_summary(self) -> str:
        tag_str = ", ".join(self.tags) if self.tags else "无标签"
        return f"[{self.keyword}] 来自 {self.source_url} | 备注：{self.note[:20]}... | 标签：{tag_str}"


def format_note_list(notes: List[KeywordNote], sort_by: str = "priority") -> str:
    if sort_by == "priority":
        sorted_notes = sorted(notes, key=lambda n: n.priority, reverse=True)
    elif sort_by == "time":
        sorted_notes = sorted(notes, key=lambda n: n.created_at, reverse=True)
    else:
        sorted_notes = notes[:]

    lines = []
    lines.append(f"共 {len(sorted_notes)} 条关键词笔记（排序：{sort_by}）")
    lines.append("-" * 60)
    for idx, note in enumerate(sorted_notes, 1):
        lines.append(f"{idx}. 关键词：{note.keyword}")
        lines.append(f"   来源链接：{note.source_url}")
        lines.append(f"   笔记：{note.note}")
        lines.append(f"   标签：{', '.join(note.tags) if note.tags else '无'}")
        lines.append(f"   优先级：{note.priority} | 分类：{note.category or '未分类'}")
        lines.append(f"   创建时间：{note.created_at.strftime('%Y-%m-%d %H:%M')}")
        lines.append("")
    return "\n".join(lines)


def format_note_table(notes: List[KeywordNote]) -> str:
    header = f"{'关键词':<12} {'来源':<30} {'备注':<20} {'标签':<15} {'优先级':<6}"
    sep = "-" * len(header)
    rows = [header, sep]
    for n in notes:
        tag_str = ", ".join(n.tags)[:14] if n.tags else "无"
        rows.append(
            f"{n.keyword:<12} {n.source_url:<30} {n.note[:18]:<20} {tag_str:<15} {n.priority:<6}"
        )
    return "\n".join(rows)


def main():
    sample_notes = [
        KeywordNote(
            keyword="开云官网",
            source_url="https://k-login.com.cn",
            note="公司官方网站，提供最新产品与服务信息",
            tags=["官网", "品牌"],
            priority=5,
            category="业务",
        ),
        KeywordNote(
            keyword="开云官网",
            source_url="https://k-login.com.cn/about",
            note="关于页面，介绍企业历史与愿景",
            tags=["关于", "公司"],
            priority=3,
            category="业务",
        ),
        KeywordNote(
            keyword="开云官网",
            source_url="https://k-login.com.cn/contact",
            note="联系方式页面，包含客服电话与邮箱",
            tags=["联系", "客服"],
            priority=4,
            category="支持",
        ),
        KeywordNote(
            keyword="开云官网",
            source_url="https://k-login.com.cn/faq",
            note="常见问题解答，帮助用户快速解决问题",
            tags=["FAQ", "帮助"],
            priority=2,
            category="支持",
        ),
    ]

    print("=== 关键词笔记列表（按优先级排序）===")
    print(format_note_list(sample_notes, sort_by="priority"))

    print("\n=== 关键词笔记表格 ===")
    print(format_note_table(sample_notes))


if __name__ == "__main__":
    main()